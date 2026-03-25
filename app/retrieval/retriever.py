from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.retrieval.schemas import Document


class TfidfRetriever:
    def __init__(self, documents: list[Document]) -> None:
        if not documents:
            raise ValueError("No documents were provided to the retriever.")

        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words="english")

        # Build TF-IDF matrix from document contents
        self.doc_matrix = self.vectorizer.fit_transform(
            [doc.content for doc in self.documents]
        )

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        """
        Return the top_k most relevant documents for the given query.
        """
        if not query.strip():
            return []

        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.doc_matrix).flatten()

        ranked_indices = scores.argsort()[::-1][:top_k]

        results = []
        for idx in ranked_indices:
            results.append(
                {
                    "doc_id": self.documents[idx].doc_id,
                    "title": self.documents[idx].title,
                    "content": self.documents[idx].content,
                    "score": float(scores[idx]),
                }
            )

        return results