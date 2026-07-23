import requests
from app.core.config import MOCK_API_BASE_URL

def create_report(report_type:str):
    r=requests.post(f"{MOCK_API_BASE_URL}/reports",json={"reportType":report_type})
    r.raise_for_status()
    return r.json()