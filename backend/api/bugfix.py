from fastapi import APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel

from backend.services.project_fix_service import ProjectFixService
from backend.services.zip_service import ZipService

router = APIRouter(
    prefix="/bugfix",
    tags=["Bug Fix"]
)


class ProjectFixRequest(BaseModel):
    project_path: str


@router.post("/project")
def fix_project(data: ProjectFixRequest):

    service = ProjectFixService()

    result = service.fix_project(
        data.project_path
    )

    # Create ZIP
    zip_path = ZipService.create_zip(
        result["fixed_project_path"]
    )

    download_url = zip_path.replace("\\", "/")

    return {

        "status": "success",

        "fixed_files": result["fixed_files"],

        "download_url": download_url

    }


@router.get("/download")
def download_fixed_project(path: str):

    return FileResponse(

        path=path,

        filename="Fixed_Project.zip",

        media_type="application/zip"

    )