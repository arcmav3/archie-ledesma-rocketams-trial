from sqlalchemy import Column,Integer,String
from app.core.database import Base

class Job(Base):
    __tablename__="jobs"
    id=Column(Integer,primary_key=True,index=True)
    report_id=Column(String,unique=True,index=True)
    report_type=Column(String)
    status=Column(String)