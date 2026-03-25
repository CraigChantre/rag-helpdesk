from app.generation.llm_client import LLMClient
from app.generation.prompts import build_helpdesk_prompt


class RAGPipeline:
    def __init__(self, retriever, llm_client: LLMClient) -> None:
        self.retriever = retriever
        self.llm_client = llm_client

    def run(self, query: str, top_k: int = 3) -> dict:
        results = self.retriever.search(query, top_k=top_k)
        context = "\n\n".join(result["content"] for result in results)
        prompt = build_helpdesk_prompt(query, context)
        answer = self.llm_client.generate(query=query, context=prompt)

        return {
            "query": query,
            "answer": answer,
            "results": results,
        }