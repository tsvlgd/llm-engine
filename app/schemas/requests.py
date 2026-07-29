from pydantic import BaseModel


class ChatRequest(BaseModel):
    query: str


class SQLRequest(BaseModel):
    question: str
    schema_context: str  # The user provides the table definitions here


class AssistantRequest(BaseModel):
    query: str
