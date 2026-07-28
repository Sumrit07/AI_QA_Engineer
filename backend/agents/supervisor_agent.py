import os
import traceback
import time
from concurrent.futures import ThreadPoolExecutor

from backend.agents.bug_detector_agent import BugDetectorAgent
from backend.agents.security_agent import SecurityAgent
from backend.agents.performance_agent import PerformanceAgent
from backend.agents.code_smell_agent import CodeSmellAgent
from backend.agents.root_cause_agent import RootCauseAgent

from backend.agents.report_generator_agent import ReportGeneratorAgent
from backend.agents.project_score_agent import ProjectScoreAgent
from backend.agents.test_generator_agent import TestGeneratorAgent
from backend.agents.test_runner_agent import TestRunnerAgent
from backend.agents.coverage_agent import CoverageAgent

from backend.services.pdf_service import PDFService
from backend.services.test_writer_service import TestWriterService


class SupervisorAgent:

    def __init__(self):

        self.bug = BugDetectorAgent()
        self.security = SecurityAgent()
        self.performance = PerformanceAgent()
        self.smell = CodeSmellAgent()
        self.root_cause = RootCauseAgent()

        self.report = ReportGeneratorAgent()
        self.score = ProjectScoreAgent()

        self.test_generator = TestGeneratorAgent()
        self.test_runner = TestRunnerAgent()
        self.coverage = CoverageAgent()

    def analyze_project(self, project_path):

        project_reports = []

        all_bugs = ""
        all_security = ""
        all_performance = ""
        all_smells = ""

        total_bugs = 0
        total_security = 0

        for root, dirs, files in os.walk(project_path):

            for file in files:

                if not file.endswith(".py"):
                    continue

                print("=" * 60)
                print(f"Analyzing : {file}")
                print("=" * 60)

                start_time = time.time()

                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    code = f.read()

                # -------------------------
                # AI Analysis
                # -------------------------

                with ThreadPoolExecutor(max_workers=5) as executor:

                    future_bug = executor.submit(self.bug.analyze, code)
                    future_security = executor.submit(self.security.analyze, code)
                    future_performance = executor.submit(self.performance.analyze, code)
                    future_smell = executor.submit(self.smell.analyze, code)
                    future_root = executor.submit(self.root_cause.analyze, code)

                    try:
                        bugs = future_bug.result()
                    except Exception:
                        traceback.print_exc()
                        bugs = "None"

                    try:
                        security = future_security.result()
                    except Exception:
                        traceback.print_exc()
                        security = "None"

                    try:
                        performance = future_performance.result()
                    except Exception:
                        traceback.print_exc()
                        performance = "None"

                    try:
                        smells = future_smell.result()
                    except Exception:
                        traceback.print_exc()
                        smells = "None"

                    try:
                        root_cause = future_root.result()
                    except Exception:
                        traceback.print_exc()
                        root_cause = "None"

                # -------------------------
                # Test Generation
                # -------------------------

                try:
                    tests = self.test_generator.generate_tests(code)
                except Exception:
                    traceback.print_exc()
                    tests = ""

                saved_test = TestWriterService.save_test(
                    file.replace(".py", ""),
                    tests
                )

                try:
                    test_result = self.test_runner.run_tests("tests/generated")
                except Exception:
                    traceback.print_exc()
                    test_result = {}

                if isinstance(bugs, list):
                    total_bugs += len(bugs)

                elif isinstance(bugs, dict):

                    if "critical" in bugs:
                        total_bugs += len(bugs.get("critical", []))
                        total_bugs += len(bugs.get("major", []))
                        total_bugs += len(bugs.get("minor", []))

                    elif bugs:
                        total_bugs += 1

                if security and security != "None":
                    total_security += 1

                project_reports.append({

                    "file": file,
                    "code": code,
                    "bugs": bugs,
                    "security": security,
                    "performance": performance,
                    "code_smells": smells,
                    "generated_tests": tests,
                    "saved_test_file": saved_test,
                    "test_results": test_result,
                    "root_cause": root_cause

                })

                import json

                all_bugs += (
                    f"\n\n### {file}\n"
                    + json.dumps(bugs, indent=2)
                )
                
                all_security += f"\n\n### {file}\n{security}"
                all_performance += f"\n\n### {file}\n{performance}"
                all_smells += f"\n\n### {file}\n{smells}"

                print(
                    f"{file} completed in "
                    f"{round(time.time() - start_time, 2)} sec"
                )

        # -------------------------
        # Coverage
        # -------------------------

        try:
            coverage = self.coverage.analyze(project_path)
        except Exception:
            traceback.print_exc()
            coverage = {
                "coverage_percent": 0
            }

        # -------------------------
        # Final Report
        # -------------------------

        report_result = self.report.generate_report(
            all_bugs,
            all_security,
            all_performance,
            all_smells
        )

        final_report = report_result.get("final_report", "")

        score_result = self.score.calculate_score(final_report)

        project_score = score_result["overall_score"]

        security_score = max(100 - total_security * 10, 0)

        print("Before PDF")

        pdf_path = PDFService.generate({

            "Project": project_path,
            "Score": project_score,
            "Coverage": coverage,
            "Final Report": final_report

        })

        print("After PDF")

        return {

            "project_path": project_path,
            "total_files": len(project_reports),
            "total_bugs": total_bugs,
            "security_score": security_score,
            "coverage": coverage,
            "project_score": project_score,
            "score_details": score_result["details"],
            "final_report": final_report,
            "pdf_report": pdf_path,
            "file_reports": project_reports,
            "executive_summary": report_result.get("executive_summary", ""),
            "overall_status": report_result.get("overall_status", ""),
            "strengths": report_result.get("strengths", []),
            "weaknesses": report_result.get("weaknesses", []),
            "recommendations": report_result.get("recommendations", [])

        }