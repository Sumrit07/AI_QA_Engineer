import os
import ast
from radon.complexity import cc_visit


class CodeAnalyzerAgent:

    def analyze_file(self, file_path):

        if not os.path.exists(file_path):
            return {
                "error": "File not found."
            }

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()

        report = {}

        # Total Lines
        report["total_lines"] = len(code.splitlines())

        # Total Functions
        tree = ast.parse(code)

        report["functions"] = len(
            [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        )

        # Total Classes
        report["classes"] = len(
            [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        )

        # Try / Except Count
        report["try_except"] = len(
            [n for n in ast.walk(tree) if isinstance(n, ast.Try)]
        )

        # Cyclomatic Complexity
        complexity = cc_visit(code)

        report["complexity"] = [
            {
                "function": c.name,
                "complexity": c.complexity
            }
            for c in complexity
        ]

        return report