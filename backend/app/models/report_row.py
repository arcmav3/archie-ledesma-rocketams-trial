from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.core.database import Base


class ReportRow(Base):
    __tablename__ = "report_rows"

    id = Column(Integer, primary_key=True, index=True)

    job_id = Column(Integer, ForeignKey("jobs.id"), index=True)

    date = Column(String)
    asin = Column(String, index=True)
    title = Column(String)

    units_ordered = Column(Integer)
    ordered_revenue = Column(Float)
    sessions = Column(Integer)
    page_views = Column(Integer)
    buy_box_pct = Column(Float)