from backend.services.gemini_service import GeminiService


class ProjectScoreAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def calculate_score(self, report):

        prompt = f"""
You are a Senior Software Quality Architect.

Analyze the following report.

Return ONLY valid JSON.

{{
    "overall_score": 0,
    "project_status": "",
    "details": {{
        "code_quality": 0,
        "security": 0,
        "performance": 0,
        "maintainability": 0
    }},
    "summary": ""
}}

Report:

{report}
"""

        try:
            result = self.gemini.generate_json(prompt)

            if result:
                return result

        except Exception as e:
            print("Project Score Error:", e)

        # -------------------------
        # Fallback Score
        # -------------------------

        return {
            "overall_score": 80,
            "project_status": "Good",
            "details": {
                "code_quality": 80,
                "security": 80,
                "performance": 80,
                "maintainability": 80
            },
            "summary": "AI score unavailable. Using fallback score."
        }