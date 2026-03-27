from pathlib import Path

from app.retrieval.loader import load_documents


def test_load_documents() -> None:
    data_dir = Path(__file__).resolve().parent.parent / "data" / "raw"
    docs = load_documents(str(data_dir))
    assert len(docs) > 0