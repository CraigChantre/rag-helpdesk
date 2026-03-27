from pathlib import Path

from app.retrieval.loader import load_documents
from app.retrieval.retriever import TfidfRetriever


def test_retriever_returns_results() -> None:
    data_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    docs = load_documents(str(data_dir))
    retriever = TfidfRetriever(docs)

    results = retriever.search("vpn help", top_k=3)

    assert len(results) > 0
    assert results[0]["title"] == "VPN Troubleshooting"