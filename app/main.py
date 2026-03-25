from app.retrieval.loader import load_documents
from app.retrieval.retriever import TfidfRetriever


def main() -> None:
    docs = load_documents("data/raw")
    retriever = TfidfRetriever(docs)

    print("Loaded documents:")
    for doc in docs:
        print(f"- {doc.title}")

    print("\nType a query, or type 'exit' to quit.\n")

    while True:
        query = input("Query: ").strip()

        if query.lower() == "exit":
            print("Goodbye.")
            break

        results = retriever.search(query, top_k=3)

        if not results:
            print("No results found.\n")
            continue

        print("\nTop results:")
        for i, result in enumerate(results, start=1):
            print(f"\n{i}. {result['title']} (score={result['score']:.4f})")
            print(result["content"][:250], "..." if len(result["content"]) > 250 else "")

        print()


if __name__ == "__main__":
    main()