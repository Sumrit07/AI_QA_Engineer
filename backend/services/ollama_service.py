import requests
import re


class OllamaService:

    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model = "qwen2.5-coder:7b"

    def fix_code(self, code: str):

        prompt = f"""
You are an expert Python software engineer.

Fix all syntax errors, bugs, formatting issues and indentation.

IMPORTANT RULES:
- Return ONLY the corrected source code.
- Do NOT explain anything.
- Do NOT write markdown.
- Do NOT use triple backticks.
- Do NOT add comments unless necessary.
- Output must be directly executable Python code.

Code:

{code}
"""

        try:

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            result = response.json()["response"].strip()

            # Remove markdown if model still returns it
            result = re.sub(r"```python", "", result)
            result = re.sub(r"```", "", result)

            return result.strip()

        except Exception as e:

            print("OLLAMA ERROR :", e)

            return code