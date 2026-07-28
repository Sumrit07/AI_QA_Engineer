from backend.services.gemini_service import GeminiService


class RootCauseAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def analyze(self, code):

        prompt = f"""
You are a Senior Software Architect.

Analyze the following Python code and identify the root cause of potential issues.

Return the result in this format:

Root Cause:
Why the issue occurs.

Impact:
What problems it can create.

Permanent Fix:
How to fix it permanently.

Best Practice:
Industry standard recommendation.

Code:

{code}
"""

        return self.gemini.generate(prompt)