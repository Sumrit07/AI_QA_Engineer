import os
import shutil

from backend.services.ollama_service import OllamaService


class ProjectFixService:

    def __init__(self):
        self.ollama = OllamaService()

    def fix_project(self, project_path):

        fixed_path = project_path.replace(
            "projects",
            "fixed_projects"
        )

        if os.path.exists(fixed_path):
            shutil.rmtree(fixed_path)

        shutil.copytree(project_path, fixed_path)

        total = 0

        for root, dirs, files in os.walk(fixed_path):

            for file in files:

                if not file.endswith(".py"):
                    continue

                filepath = os.path.join(root, file)

                with open(
                    filepath,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    code = f.read()

                print(f"Fixing {file}")

                fixed = self.ollama.fix_code(code)

                with open(
                    filepath,
                    "w",
                    encoding="utf-8"
                ) as f:

                    f.write(fixed)

                total += 1

        return {

            "status": "success",

            "fixed_files": total,

            "fixed_project_path": fixed_path

        }