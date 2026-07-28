from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.upload_service import UploadService
from backend.services.project_service import ProjectService
from backend.database.database import SessionLocal

import os
import shutil
import uuid

router = APIRouter(
    prefix="/upload",
    tags=["Project Upload"]
)

UPLOAD_DIR = "projects"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/zip")
async def upload_zip(file: UploadFile = File(...)):

    if not file.filename.endswith(".zip"):
        raise HTTPException(
            status_code=400,
            detail="Only ZIP files are allowed."
        )

    project_id = str(uuid.uuid4())

    project_folder = os.path.join(UPLOAD_DIR, project_id)
    os.makedirs(project_folder, exist_ok=True)

    zip_path = os.path.join(project_folder, file.filename)

    try:

        with open(zip_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        UploadService.extract_zip(zip_path, project_folder)

        db = SessionLocal()

        try:

            project_service = ProjectService(db)

            project_service.create_project(

                project_name=file.filename.replace(".zip", ""),

                project_id=project_id,

                framework="Python",

                total_files=0,

                upload_path=project_folder

            )

        finally:
            db.close()

        return {

            "status": "success",

            "project_id": project_id,

            "project_name": file.filename.replace(".zip", ""),

            "project_path": project_folder,

            "message": "Project uploaded successfully."

        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )