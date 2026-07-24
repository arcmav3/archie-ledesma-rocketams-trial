import asyncio
import httpx
import gzip
import csv
import io

BASE_URL = "http://127.0.0.1:9000"


async def create_report():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/reports",
            json={
                "reportType": "SALES_AND_TRAFFIC"
            }
        )

        response.raise_for_status()

        return response.json()


async def get_report_status(report_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/reports/{report_id}"
        )

        response.raise_for_status()

        return response.json()

async def wait_for_report(report_id: str):
    while True:
        await asyncio.sleep(2)

        status = await get_report_status(report_id)

        processing_status = status["processingStatus"]

        print(f"Status: {processing_status}")

        if processing_status == "DONE":
            return status

        if processing_status == "FATAL":
            raise Exception("Report generation failed.")

async def download_report(report_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{BASE_URL}/reports/{report_id}/document"
        )

        response.raise_for_status()

        return response.content

def unzip_report(report_file: bytes) -> str:
    return gzip.decompress(report_file).decode("utf-8")

def parse_report(report_text: str):
    reader = csv.DictReader(
        io.StringIO(report_text),
        delimiter="\t"
    )

    return list(reader)