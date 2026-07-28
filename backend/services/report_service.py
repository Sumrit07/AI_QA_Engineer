import json

from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.report import Report


class ReportService:

    @staticmethod
    def save_report(data):

        db: Session = SessionLocal()

        try:

            report = Report(

                project_id=data["project_id"],

                project_name=data["project_name"],

                score=str(data["project_score"]),

                coverage=str(data["coverage"]),

                total_files=data["total_files"],

                final_report=data["final_report"],

                pdf_path=data["pdf_report"],
                
                analysis_json=json.dumps(data["analysis"])

            )

            db.add(report)
            db.commit()
            db.refresh(report)

            return report

        except Exception as e:

            db.rollback()
            raise e

        finally:
            db.close()

    @staticmethod
    def get_reports():

        db: Session = SessionLocal()

        try:

            reports = db.query(Report).order_by(
                Report.created_at.desc()
            ).all()

            return reports

        finally:
            db.close()

    @staticmethod
    def get_history():

        db: Session = SessionLocal()

        try:

            history = db.query(Report).order_by(
                Report.created_at.desc()
            ).all()

            return history

        finally:
            db.close()

    @staticmethod
    def get_report(report_id: int):

        db: Session = SessionLocal()

        try:

            return db.query(Report).filter(
                Report.id == report_id
            ).first()

        finally:
            db.close()

    @staticmethod
    def delete_report(report_id: int):

        db: Session = SessionLocal()

        try:

            report = db.query(Report).filter(
                Report.id == report_id
            ).first()

            if not report:
                return False

            db.delete(report)
            db.commit()

            return True

        finally:
            db.close()