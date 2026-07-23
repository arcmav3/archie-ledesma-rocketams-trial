from pydantic import BaseModel

class ReportRowResponse(BaseModel):
    date:str
    asin:str
    title:str