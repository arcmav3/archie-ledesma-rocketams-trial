from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.jobs import router as jobs_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RocketAMS Backend")

app.include_router(jobs_router, prefix="/api")

@app.get("/")
def root():
    return {"status":"running"}