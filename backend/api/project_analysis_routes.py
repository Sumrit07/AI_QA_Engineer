from fastapi import APIRouter, HTTPException
import os
import traceback

from backend.agents.project_analyzer_agent import ProjectAnalyzerAgent
from backend.services.report_service import ReportService

from backend.services.project_service import ProjectService
from backend.database.database import SessionLocal

router = APIRouter(
    prefix="/analysis",
    tags=["Project Analysis"]
)

analyzer = ProjectAnalyzerAgent()


@router.post("/project/{project_id}")
def analyze_project(project_id: str):

    project_path = os.path.join("projects", project_id)

    if not os.path.exists(project_path):
        raise HTTPException(
            status_code=404,
            detail="Project not found."
        )

    try:

        result = analyzer.analyze_project(project_path)

        db = SessionLocal()

        try:
            project_service = ProjectService(db)

            project = project_service.get_project(project_id)

            project_name = (
                project.project_name
                if project
                else os.path.basename(project_path)
            )

        finally:
            db.close()

        ReportService.save_report({

            "project_id": project_id,

            "project_name": project_name,

            "project_score": result.get("project_score", 0),

            "coverage": str(result.get("coverage", "")),

            "total_files": result.get("total_files", 0),

            "final_report": result.get("final_report", ""),

            "pdf_report": result.get("pdf_report", ""),
            
            "analysis": result

        })

        return {

            "status": "success",

            "message": "Project analyzed successfully.",

            "project_id": project_id,

            "analysis": result

        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=f"Analysis Failed : {str(e)}"
        )