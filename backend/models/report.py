from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.database.base import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    project_id = Column(
        String,
        ForeignKey("projects.project_id"),
        nullable=False
    )

    project_name = Column(String, nullable=False)

    score = Column(String)

    coverage = Column(String)

    total_files = Column(Integer)

    final_report = Column(Text)

    pdf_path = Column(String)
    
    analysis_json = Column(Text)
    
    

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    project = relationship(
        "Project",
        back_populates="reports"
    )