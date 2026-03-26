from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str


class RetrievedDocument(BaseModel):
    doc_id: str
    title: str
    content: str
    score: float


class QueryResponse(BaseModel):
    query: str
    answer: str
    sources: list[str]
    results: list[RetrievedDocument]