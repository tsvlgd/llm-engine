from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.requests import ChatRequest
from app.schemas.responses import ChatResponse
from app.services.chat import generate_message, generate_stream

router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def res_chat(request: ChatRequest):
    return await generate_message(request.query)


@router.post("/stream")
# Streaming responses are handled differently because they send chunks, so better not to intrduce here.
async def res_steram(request: ChatRequest):
    return StreamingResponse(
        generate_stream(request.query), media_type="text/event-stream"
    )
