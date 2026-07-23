from app.services.mock_api import create_report

def submit_job(report_type:str):
    return create_report(report_type)