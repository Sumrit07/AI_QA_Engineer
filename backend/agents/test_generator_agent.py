from backend.services.gemini_service import GeminiService
from backend.prompts.test_generator_prompt import TEST_GENERATOR_PROMPT


class TestGeneratorAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_tests(self, code: str):

        prompt = TEST_GENERATOR_PROMPT.format(
            code=code
        )

        return self.gemini.generate(prompt)