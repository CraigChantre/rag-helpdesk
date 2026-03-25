from pathlib import Path

from fastapi import FastAPI

from app.api.schemas import QueryRequest, QueryResponse, RetrievedDocument
from app.retrieval.loader import load_documents
from app.retrieval.retriever import TfidfRetriever
from app.generation.llm_client import LLMClient
from app.services.rag_pipeline import RAGPipeline

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

docs = load_documents(str(DATA_DIR))
retriever = TfidfRetriever(docs)

app = FastAPI(title="RAG Helpdesk API")
llm_client = LLMClient()
pipeline = RAGPipeline(retriever, llm_client)

@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "documents_loaded": len(docs),
    }


@app.post("/query")
def query_docs(request: QueryRequest):
    response = pipeline.run(request.query)
    return response