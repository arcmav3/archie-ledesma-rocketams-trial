import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL","sqlite:///./reports.db")
MOCK_API_BASE_URL = os.getenv("MOCK_API_BASE_URL","http://localhost:9000")