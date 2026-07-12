from typing import Optional
from pydantic import BaseModel


class ChatResponse(BaseModel):
    answer: str
    model: str


class SummarizeResponse(BaseModel):
    summary: str
    key_points: Optional[list[str]] = None
    action_items: Optional[list[str]] = None
    language: Optional[str] = None
