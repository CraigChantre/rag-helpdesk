from pathlib import Path

from fastapi import FastAPI

from app.api.schemas import QueryRequest, QueryResponse, RetrievedDocument
from app.generation.llm_client import LLMClient
from app.retrieval.loader import load_documents
from app.retrieval.retriever import TfidfRetriever
from app.services.rag_pipeline import RAGPipeline


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"

docs = load_documents(str(DATA_DIR))
retriever = TfidfRetriever(docs)
llm_client = LLMClient()
pipeline = RAGPipeline(retriever, llm_client)

app = FastAPI(title="RAG Helpdesk API")


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "documents_loaded": len(docs),
    }


@app.post("/query", response_model=QueryResponse)
def query_docs(request: QueryRequest) -> QueryResponse:
    response = pipeline.run(request.query)

    results = [
        RetrievedDocument(
            doc_id=result["doc_id"],
            title=result["title"],
            content=result["content"],
            score=result["score"],
        )
        for result in response["results"]
    ]

    return QueryResponse(
        query=response["query"],
        answer=response["answer"],
        sources=response["sources"],
        results=results,
    )