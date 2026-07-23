from fastapi import APIRouter
from app.schemas.job import CreateJobRequest
from app.services.report_service import submit_job

router=APIRouter(tags=["jobs"])

@router.post("/jobs")
def create_job(body:CreateJobRequest):
    return submit_job(body.reportType)