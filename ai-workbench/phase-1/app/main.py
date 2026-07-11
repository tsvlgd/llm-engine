from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse
from app.chat import generate_message, generate_stream
from app.schemas import ChatRequest
from app.core.config import settings

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Workbench is running"}


@app.post("/chat")
async def res_chat(request: ChatRequest):
    result = await generate_message(request.query)
    return result


@app.post("/stream")
async def res_steram(request: ChatRequest):
    return StreamingResponse(
        generate_stream(request.query), media_type="text/event-stream"
    )


@app.get("/health")
def get_health():
    return {
        "status": "Okay",
        "service": "API",
        "version": "0.1",
        "provider": f"{settings.model.split('/')[0]}",
        "model": f"{settings.model.split('/')[1]}",
    }
