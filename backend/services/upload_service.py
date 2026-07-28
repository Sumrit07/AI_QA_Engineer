import os
import zipfile


class UploadService:

    @staticmethod
    def extract_zip(zip_path: str, extract_to: str):

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)

        return extract_to