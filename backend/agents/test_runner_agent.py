import subprocess
import time
import os


class TestRunnerAgent:

    def run_tests(self, test_path="tests/generated"):

        if not os.path.exists(test_path):
            return {
                "status": "Skipped",
                "execution_time": 0,
                "output": "",
                "errors": f"Test folder '{test_path}' not found."
            }

        start = time.time()

        result = subprocess.run(
            ["pytest", test_path, "-v"],
            capture_output=True,
            text=True
        )

        end = time.time()

        return {
            "status": "Passed" if result.returncode == 0 else "Failed",
            "execution_time": round(end - start, 2),
            "output": result.stdout,
            "errors": result.stderr
        }