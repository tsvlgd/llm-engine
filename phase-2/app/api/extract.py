from fastapi import APIRouter, Body
from app.services.extractor import perform_extraction
from app.schemas.responses import ExtractResponse

router = APIRouter()


@router.post("/", response_model=ExtractResponse)
async def extract(text: str = Body(..., media_type="text/plain")):
    return await perform_extraction(text)
