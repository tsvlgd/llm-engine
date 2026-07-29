from fastapi import APIRouter, Body
from app.services.code import perform_code_explanation
from app.schemas.responses import CodeExplainResponse

router = APIRouter()


@router.post("/explain", response_model=CodeExplainResponse)
async def extract(code: str = Body(..., media_type="text/plain")):
    return await perform_code_explanation(code)
