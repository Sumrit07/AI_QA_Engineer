from sqlalchemy.orm import Session

from backend.database.models import Project
from backend.schemas.project_schema import ProjectCreate


class ProjectRepository:

    @staticmethod
    def create_project(db: Session, project: ProjectCreate):

        db_project = Project(
            name=project.name,
            github_url=str(project.github_url) if project.github_url else None,
            language=project.language,
            status="Pending"
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)

        return db_project