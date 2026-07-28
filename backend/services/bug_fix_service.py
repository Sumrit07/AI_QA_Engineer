import traceback
import ollama


class BugFixService:

    def __init__(self):

        self.model = "qwen2.5-coder:7b"

        print("=" * 50)
        print("Bug Fix Service Initialized")
        print("Model :", self.model)
        print("=" * 50)

    # -----------------------------------
    # Auto Bug Fix
    # -----------------------------------

    def fix_code(self, code: str, language="python"):

        prompt = f"""
You are an expert software engineer.

Your task is to fix the following {language} code.

Rules:
1. Fix all syntax errors.
2. Fix logical bugs if found.
3. Do not change functionality.
4. Return ONLY the corrected code.
5. Do not explain anything.
6. Do not use markdown.

Code:

{code}
"""

        try:

            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception:

            traceback.print_exc()

            return None