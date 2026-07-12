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


class EntityItem(BaseModel):
    name: str
    type: str


class ExtractResponse(BaseModel):
    category: str
    entities: list[EntityItem]
    confidence_score: float


class CodeExplainResponse(BaseModel):
    summary: str
    time_complexity: str
    space_complexity: str
    vulnerabilities: Optional[list[str]] = None


class SQLResponse(BaseModel):
    sql_query: str
    explanation: str
    target_database: Optional[str] = None  # e.g., "PostgreSQL", "MySQL", "SQLite
