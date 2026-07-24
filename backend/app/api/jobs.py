from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.job import Job

from app.services.report_service import (
    create_report,
    #get_report_status,
    wait_for_report,
    download_report,
    unzip_report,
    parse_report,
)

from app.models.report_row import ReportRow



router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/jobs")
async def create_job(db: Session = Depends(get_db)):
    job = Job(
        status="pending"
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    job.status = "processing"
    db.commit()
    db.refresh(job)

    report = await create_report()
    report_id = report["reportId"]

    job.external_job_id = report["reportId"]
    job.report_url = f"http://127.0.0.1:9000/reports/{report_id}/document"
    db.commit()
    db.refresh(job)

    await wait_for_report(report_id)
    
    # Call the mock report API
    #report = await get_report_status(report_id)

    # download report
    report_file = await download_report(report_id)
    #print(f"Downloaded {len(report_file)} bytes")

    report_text = unzip_report(report_file)
    #print(report_text)

    rows = parse_report(report_text)
    #print(rows[0])

    for row in rows:
        report_row = ReportRow(
            job_id=job.id,
            date=row["date"],
            asin=row["asin"],
            title=row["title"],
            units_ordered=int(row["units_ordered"]),
            ordered_revenue=float(row["ordered_revenue"]),
            sessions=int(row["sessions"]),
            page_views=int(row["page_views"]),
            buy_box_pct=float(row["buy_box_pct"]),
        )

        db.add(report_row)
    db.commit()

    job.status = "completed"
    db.commit()
    db.refresh(job)

    return {
        "job_id": job.id,
        "rows": len(rows),
        "first_row": rows[0],
        "status": job.status
    }

@router.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(Job).all()

    return jobs

@router.get("/jobs/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job

@router.get("/jobs/{job_id}/report")
def get_job_report(job_id: int, db: Session = Depends(get_db)):
    rows = (
        db.query(ReportRow)
        .filter(ReportRow.job_id == job_id)
        .all()
    )

    return rows