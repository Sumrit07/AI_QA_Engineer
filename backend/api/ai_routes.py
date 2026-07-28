from fastapi import APIRouter

from backend.services.gemini_service import GeminiService
from backend.agents.supervisor_agent import SupervisorAgent

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

gemini = GeminiService()
analyzer = SupervisorAgent()


@router.post("/test")
def test_ai():

    prompt = """
    Explain what FastAPI is in 5 lines.
    """

    answer = gemini.generate(prompt)

    return {
        "response": answer
    }


@router.post("/analyze")
def analyze():

    # Upload hone wale project ka path
    project_path = "projects"

    result = analyzer.analyze_project(project_path)

    return result