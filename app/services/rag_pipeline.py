from app.generation.llm_client import LLMClient
from app.generation.prompts import build_helpdesk_prompt


class RAGPipeline:
    def __init__(self, retriever, llm_client: LLMClient) -> None:
        self.retriever = retriever
        self.llm_client = llm_client

    def run(self, query: str, top_k: int = 3) -> dict:
        results = self.retriever.search(query, top_k=top_k)

        # Keep only relevant results
        results = [r for r in results if r["score"] > 0.1]

        # If nothing relevant is found, return a safe fallback
        if not results:
            return {
                "query": query,
                "answer": "I’m not sure based on the available documentation.",
                "sources": [],
                "results": [],
            }

        # For now, keep context small and grounded
        results = results[:1]

        context = "\n\n".join(result["content"] for result in results)
        prompt = build_helpdesk_prompt(query, context)
        answer = self.llm_client.generate(query=query, context=prompt)

        sources = [result["title"] for result in results]

        return {
            "query": query,
            "answer": answer.strip(),
            "sources": sources,
            "results": results,
        }