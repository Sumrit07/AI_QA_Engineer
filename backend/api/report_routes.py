import json

from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, HTTPException

from backend.services.report_service import ReportService

from fastapi import Depends
from backend.dependencies.auth import get_current_user


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/")
def get_reports():
    return ReportService.get_reports()


@router.get("/history")
def get_history():
    return ReportService.get_history()


# ==========================
# Delete Report
# ==========================

@router.delete("/{report_id}")
def delete_report(report_id: int):

    deleted = ReportService.delete_report(report_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return {
        "status": "success",
        "message": "Report deleted successfully"
    }
    
    
    
    
    
# (Get_Reports)


@router.get("/{report_id}")
def get_report(report_id: int):

    report = ReportService.get_report(report_id)

    if not report:
        return {
            "status": "error",
            "message": "Report Not Found"
        }

    report = jsonable_encoder(report)

    report["analysis_json"] = json.loads(
        report["analysis_json"]
    )

    return {
        "status": "success",
        "report": report
    }