from sqlalchemy.orm import Session
from sqlalchemy import func, Integer

from backend.database.database import SessionLocal
from backend.models.project import Project
from backend.models.report import Report


class DashboardService:

    @staticmethod
    def get_stats():

        db: Session = SessionLocal()

        try:

            # Total Projects
            total_projects = db.query(Project).count()

            # Total Reports
            total_reports = db.query(Report).count()

            # Average Score
            avg_score = db.query(
                func.avg(Report.score.cast(Integer))
            ).scalar()

            # Latest Report
            latest_report = (
                db.query(Report)
                .order_by(Report.created_at.desc())
                .first()
            )

            if latest_report:

                last_scan = latest_report.created_at.strftime(
                    "%d %b %Y | %I:%M %p"
                )

            else:

                last_scan = "--"

            return {

                "total_projects": total_projects,

                "total_reports": total_reports,

                "average_score": round(avg_score or 0),

                "last_scan": last_scan

            }

        finally:

            db.close()