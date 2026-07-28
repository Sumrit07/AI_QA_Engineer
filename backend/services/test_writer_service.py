import os


class TestWriterService:

    @staticmethod
    def save_test(file_name, test_code):

        os.makedirs("tests/generated", exist_ok=True)

        if not file_name.startswith("test_"):
            file_name = f"test_{file_name}"

        if not file_name.endswith(".py"):
            file_name += ".py"

        path = os.path.join("tests/generated", file_name)

        with open(path, "w", encoding="utf-8") as f:
            f.write(str(test_code))

        return path