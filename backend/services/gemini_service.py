import os
import traceback
from google import genai
from dotenv import load_dotenv

from backend.utils.json_parser import parse_json

load_dotenv()


class GeminiService:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file.")

        print("=" * 50)
        print("Gemini Service Initialized")
        print("API KEY :", api_key[:15] + "********")
        print("=" * 50)

        self.client = genai.Client(api_key=api_key)

        self.model = "gemini-2.5-flash"

    # -----------------------------------
    # Normal Text Response
    # -----------------------------------

    def generate(self, prompt: str):

        print("\nCalling Gemini API...")

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            print("Gemini API Success")

            if hasattr(response, "text"):
                print("Response Preview:")
                print(response.text[:300])
                print("-" * 50)

            if hasattr(response, "text") and response.text:
                return response.text.strip()

            print("Empty response received.")
            return ""

        except Exception:

            print("\n" + "=" * 60)
            print("GEMINI API ERROR")
            traceback.print_exc()
            print("=" * 60 + "\n")

            return ""

    # -----------------------------------
    # JSON Response
    # -----------------------------------

    def generate_json(self, prompt: str):

        text = self.generate(prompt)

        if not text:
            return None

        try:

            parsed = parse_json(text)

            print("JSON Parsed Successfully")

            return parsed

        except Exception:

            print("\nJSON Parse Failed")
            traceback.print_exc()

            return None