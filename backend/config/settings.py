"""
Application Configuration
"""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class Settings:

    APP_NAME = os.getenv("APP_NAME", "AI QA Engineer")

    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    DEBUG = os.getenv("DEBUG", "True") == "True"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/ai_qa_engineer"
    )


settings = Settings()