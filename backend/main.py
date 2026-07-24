from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.models.job import Job
from app.models.report_row import ReportRow

from app.api.jobs import router as jobs_router



app = FastAPI(title="RocketAMS Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:8000/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

app.include_router(jobs_router)

@app.get("/")
def root():
    return {"message": "RocketAMS Backend Running"}