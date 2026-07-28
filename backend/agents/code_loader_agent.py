import os


class CodeLoaderAgent:

    IGNORE_FOLDERS = {
        ".git",
        "venv",
        "__pycache__",
        "node_modules",
        ".idea",
        ".vscode"
    }

    PYTHON_EXTENSIONS = {
        ".py"
    }

    @staticmethod
    def scan_project(project_path):

        project_info = {
            "project_name": os.path.basename(project_path),
            "python_files": [],
            "total_files": 0,
            "framework": "Unknown"
        }

        for root, dirs, files in os.walk(project_path):

            dirs[:] = [
                d for d in dirs
                if d not in CodeLoaderAgent.IGNORE_FOLDERS
            ]

            for file in files:

                project_info["total_files"] += 1

                filepath = os.path.join(root, file)

                if file.endswith(".py"):

                    project_info["python_files"].append(filepath)

                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:

                        code = f.read()

                        if "FastAPI(" in code:
                            project_info["framework"] = "FastAPI"

                        elif "Flask(" in code:
                            project_info["framework"] = "Flask"

                        elif "django" in code.lower():
                            project_info["framework"] = "Django"

        return project_info