from typing import TypedDict


class QAState(TypedDict):

    project_id: str

    project_path: str

    framework: str

    python_files: list

    analysis: dict

    security_report: dict

    test_cases: list

    coverage: dict

    bugs: list

    root_cause: dict

    final_report: dict