import requests


class LLMClient:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.1:8b"):
        self.base_url = base_url
        self.model = model

    def generate(self, query: str, context: str) -> str:
        prompt = context  # context already includes query + instructions

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120,
        )

        response.raise_for_status()
        data = response.json()

        return data["response"]