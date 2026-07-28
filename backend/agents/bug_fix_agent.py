from backend.services.bug_fix_service import BugFixService


class BugFixAgent:

    def __init__(self):
        self.service = BugFixService()

    def fix_file(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            original_code = f.read()

        fixed_code = self.service.fix_code(original_code)

        return {
            "file": file_path,
            "original_code": original_code,
            "fixed_code": fixed_code
        }