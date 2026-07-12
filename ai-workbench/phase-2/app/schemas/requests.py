from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str


class SummarizeRequest(BaseModel):
    text: str
