from sqlalchemy.orm import Session

from backend.models.project import Project


class ProjectService:

    def __init__(self, db: Session):
        self.db = db

    def create_project(
        self,
        project_name,
        project_id,
        framework,
        total_files,
        upload_path
    ):

        project = Project(
            project_name=project_name,
            project_id=project_id,
            framework=framework,
            total_files=total_files,
            upload_path=upload_path
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def get_project(self, project_id: str):

        return (
            self.db.query(Project)
            .filter(Project.project_id == project_id)
            .first()
        )