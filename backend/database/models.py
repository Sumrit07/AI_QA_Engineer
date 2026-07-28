from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from backend.database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    github_url = Column(String, nullable=True)

    language = Column(String, nullable=False)

    status = Column(String, default="Pending")

    local_path = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)