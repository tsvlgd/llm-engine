from fastapi import APIRouter

from app.schemas.requests import AssistantRequest
from app.schemas.responses import AssistantResponse
from app.services.assistant import run_assistant

router = APIRouter()


@router.post("/", response_model=AssistantResponse)
async def assistant(request: AssistantRequest):

    return await run_assistant(request.query)
