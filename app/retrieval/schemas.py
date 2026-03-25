from dataclasses import dataclass

@dataclass
class Document:
    doc_id: str
    title: str
    content: str
    