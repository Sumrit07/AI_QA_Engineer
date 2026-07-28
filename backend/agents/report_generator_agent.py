from backend.services.gemini_service import GeminiService


class ReportGeneratorAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_report(
        self,
        bug_report,
        security_report,
        performance_report,
        smell_report
    ):

        prompt = f"""
You are a Senior Software QA Lead.

Analyze the following reports and generate ONE final software quality report.

Return ONLY valid JSON.

{{
    "executive_summary": "",
    "overall_status": "",
    "strengths": [""],
    "weaknesses": [""],
    "recommendations": [
        "",
        "",
        "",
        "",
        ""
    ],
    "final_report": ""
}}

=========================
BUG REPORT
=========================

{bug_report}

=========================
SECURITY REPORT
=========================

{security_report}

=========================
PERFORMANCE REPORT
=========================

{performance_report}

=========================
CODE SMELLS
=========================

{smell_report}
"""

        try:

            result = self.gemini.generate_json(prompt)

            if result:
                return result

        except Exception as e:

            print("Report Generator Error:", e)

        # ------------------------------
        # Fallback Report
        # ------------------------------

        return {

            "executive_summary":
                "AI report could not be generated because the Gemini API is unavailable or quota has been exceeded.",

            "overall_status":
                "Needs Improvements",

            "strengths": [
                "Project analysis completed successfully.",
                "Bug scanning completed.",
                "Security scanning completed.",
                "Performance analysis completed.",
                "Code smell detection completed."
            ],

            "weaknesses": [
                "AI-generated summary unavailable."
            ],

            "recommendations": [
                "Fix detected bugs.",
                "Resolve security issues.",
                "Improve code quality.",
                "Optimize performance.",
                "Retry AI report generation after API quota resets."
            ],

            "final_report": f"""
SOFTWARE QUALITY REPORT

BUG REPORT

{bug_report}

SECURITY REPORT

{security_report}

PERFORMANCE REPORT

{performance_report}

CODE SMELLS

{smell_report}

NOTE:
AI-generated report could not be produced because the Gemini API quota was exceeded.
"""

        }