from fastapi import FastAPI

from app import __description__, __title__, __version__
from app.api import assistant, chat, code, extract, sql, summarize
from app.core.config import settings
from app.tools.registry import registry

app = FastAPI(
    title=__title__,
    description=__description__,
    version=__version__,
)
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])
app.include_router(extract.router, prefix="/extract", tags=["extract"])
app.include_router(sql.router, prefix="/sql", tags=["SQL"])
app.include_router(code.router, prefix="/code", tags=["Explainer"])
app.include_router(assistant.router, prefix="/assistant", tags=["Assistant"])


@app.get("/")
def home():
    return {"message": "AI Workbench is running"}


@app.get("/health")
def get_health():
    provider, model = settings.model.split("/")
    return {
        "status": "Okay",
        "service": "API",
        "version": __version__,
        "provider": provider,
        "model": model,
        "tools integrated": registry.tool_count(),
    }
