from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    project_name = Column(String, nullable=False)

    project_id = Column(String, unique=True, nullable=False)

    framework = Column(String)

    total_files = Column(Integer)

    upload_path = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    reports = relationship(
        "Report",
        back_populates="project",
        cascade="all, delete-orphan"
    )