def build_helpdesk_prompt(query: str, context: str) -> str:
    return f"""
You are an IT helpdesk assistant.

Use only the provided context to answer the user's question.
If the answer is not in the context, say you are not sure.

User question:
{query}

Context:
{context}

Answer:
""".strip()