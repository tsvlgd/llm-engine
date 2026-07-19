from fastapi import APIRouter, Body
from app.services.summarizer import perform_summary
from app.schemas.responses import SummarizeResponse

router = APIRouter()


@router.post("/", response_model=SummarizeResponse)
async def res_summary(text: str = Body(..., media_type="text/plain")):
    return await perform_summary(text)
