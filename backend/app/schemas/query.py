from pydantic import BaseModel
from typing import Optional


class QueryRequest(BaseModel):
    question: str
    outfit_context: Optional[str] = None


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]