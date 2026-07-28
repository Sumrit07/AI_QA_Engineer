import os
import shutil


class ZipService:

    @staticmethod
    def create_zip(project_folder):

        if not os.path.exists(project_folder):
            raise FileNotFoundError(
                f"Folder not found : {project_folder}"
            )

        zip_path = project_folder

        # Remove old zip if exists
        if os.path.exists(zip_path + ".zip"):
            os.remove(zip_path + ".zip")

        shutil.make_archive(

            base_name=zip_path,

            format="zip",

            root_dir=project_folder

        )

        return zip_path + ".zip"