from fastapi import FastAPI
from app.api import chat
from app.api import summarize
from app.core.config import settings

app = FastAPI(title="AI Workbench")

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])


@app.get("/")
def home():
    return {"message": "AI Workbench is running"}


@app.get("/health")
def get_health():
    provider, model = settings.model.split("/")
    return {
        "status": "Okay",
        "service": "API",
        "version": "0.1",
        "provider": provider,
        "model": model,
    }
