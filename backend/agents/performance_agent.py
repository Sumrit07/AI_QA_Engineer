from backend.services.gemini_service import GeminiService


class PerformanceAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def analyze(self, code: str):

        prompt = f"""
You are a Python Performance Engineer.

Analyze performance problems.

Return ONLY JSON.

{{
    "performance":[
        {{
            "issue":"",
            "impact":"",
            "optimization":""
        }}
    ]
}}

Python Code:

{code}
"""

        return self.gemini.generate_json(prompt)