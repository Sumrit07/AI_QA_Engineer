import os
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PDFService:

    @staticmethod
    def generate(report_data, filename="report.pdf"):

        os.makedirs("reports", exist_ok=True)

        pdf_path = os.path.join("reports", filename)

        doc = SimpleDocTemplate(pdf_path)

        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("<b>AI QA Engineer Report</b>", styles["Title"]))

        story.append(Paragraph("<br/>", styles["Normal"]))

        for key, value in report_data.items():

            story.append(
                Paragraph(f"<b>{key}</b>", styles["Heading2"])
            )

            story.append(
                Paragraph(str(value), styles["BodyText"])
            )

            story.append(
                Paragraph("<br/>", styles["Normal"])
            )

        doc.build(story)

        return pdf_path