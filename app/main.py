from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

from app.retrieval.loader import load_documents
from app.retrieval.retriever import TfidfRetriever


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

docs = load_documents(str(DATA_DIR))
retriever = TfidfRetriever(docs)

app = FastAPI(title="RAG Helpdesk API")


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "documents_loaded": len(docs),
    }


@app.post("/query")
def query_docs(request: QueryRequest) -> dict:
    results = retriever.search(request.query, top_k=3)
    return {
        "query": request.query,
        "results": results,
    }