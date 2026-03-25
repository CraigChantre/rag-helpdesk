from pathlib import Path

from app.retrieval.schemas import Document


def load_documents(data_dir: str) -> list[Document]:
    """
    Load all .txt documents from the given directory.

    Expected format:
    First line: Title: Some Title
    Remaining lines: document content
    """
    docs: list[Document] = []
    base_path = Path(data_dir)

    if not base_path.exists():
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    for path in sorted(base_path.glob("*.txt")):
        text = path.read_text(encoding="utf-8").strip()

        if not text:
            continue

        lines = text.splitlines()

        # Default title from filename
        title = path.stem.replace("_", " ").title()
        content = text

        # If first line starts with "Title:", use it
        if lines and lines[0].lower().startswith("title:"):
            title = lines[0].split(":", 1)[1].strip()
            content = "\n".join(lines[1:]).strip()

        docs.append(
            Document(
                doc_id=path.stem,
                title=title,
                content=content,
            )
        )

    return docs