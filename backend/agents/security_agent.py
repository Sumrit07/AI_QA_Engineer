from backend.services.gemini_service import GeminiService


class SecurityAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def analyze(self, code: str):

        prompt = f"""
You are a Senior Cyber Security Engineer.

Analyze the Python code.

Return ONLY JSON.

{{
    "security":[
        {{
            "issue":"",
            "severity":"",
            "risk":"",
            "solution":""
        }}
    ]
}}

Python Code:

{code}
"""

        return self.gemini.generate_json(prompt)