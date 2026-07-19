from fastapi import APIRouter, Body, status
from app.services.sql import perform_sql_generation
from app.schemas.requests import SQLRequest
from app.schemas.responses import SQLResponse

router = APIRouter()


@router.post("/generate", response_model=SQLResponse, status_code=status.HTTP_200_OK)
async def generate(request: SQLRequest):
    return await perform_sql_generation(request)
