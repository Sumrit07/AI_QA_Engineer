from backend.prompts.bug_detector_prompt import BUG_DETECTOR_PROMPT
from backend.services.gemini_service import GeminiService


class BugDetectorAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def analyze(self, code):

        prompt = BUG_DETECTOR_PROMPT.format(
            code=code
        )

        try:

            result = self.gemini.generate_json(prompt)

            if result:
                return result

        except Exception as e:

            print("Bug Detector Error:", e)

        # ----------------------------
        # Fallback
        # ----------------------------

        return {
            "status": "No Bugs Found",
            "critical": [],
            "major": [],
            "minor": [],
            "summary": "AI bug detection unavailable."
        }