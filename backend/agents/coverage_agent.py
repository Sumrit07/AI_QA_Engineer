import os


class CoverageAgent:

    def analyze(self, project_path):

        python_files = []
        test_files = []

        for root, dirs, files in os.walk(project_path):

            for file in files:

                if file.endswith(".py"):

                    full_path = os.path.join(root, file)

                    if "test" in file.lower():
                        test_files.append(full_path)
                    else:
                        python_files.append(full_path)

        total_files = len(python_files)

        tested_files = min(len(test_files), total_files)

        if total_files == 0:
            coverage = 0
        else:
            coverage = round((tested_files / total_files) * 100, 2)

        untested = python_files[tested_files:]

        return {
            "total_python_files": total_files,
            "test_files": len(test_files),
            "coverage_percent": coverage,
            "untested_files": untested
        }