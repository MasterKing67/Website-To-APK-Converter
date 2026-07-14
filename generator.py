"""
generator.py

Copies an Android Studio template project and customizes it.

Author: Shiny Studios
"""

from pathlib import Path
import shutil


class ProjectGenerator:
    def __init__(self, template_folder="android_template"):
        self.template = Path(template_folder)

    def generate(
        self,
        app_name,
        package_name,
        website_url,
        output_folder,
        icon_path=None,
    ):
        if not self.template.exists():
            raise FileNotFoundError(
                f"Template folder not found: {self.template}"
            )

        destination = Path(output_folder) / app_name

        if destination.exists():
            shutil.rmtree(destination)

        shutil.copytree(self.template, destination)

        self.replace_placeholders(
            destination,
            app_name,
            package_name,
            website_url,
        )

        if icon_path:
            self.copy_icon(destination, icon_path)

        return destination

    def replace_placeholders(
        self,
        folder,
        app_name,
        package_name,
        website_url,
    ):
        replacements = {
            "{APP_NAME}": app_name,
            "{PACKAGE_NAME}": package_name,
            "{WEBSITE_URL}": website_url,
        }

        for file in folder.rglob("*"):

            if file.suffix.lower() not in (
                ".kt",
                ".xml",
                ".gradle",
                ".properties",
                ".txt",
            ):
                continue

            try:
                text = file.read_text(encoding="utf-8")

                for key, value in replacements.items():
                    text = text.replace(key, value)

                file.write_text(text, encoding="utf-8")

            except Exception:
                pass

    def copy_icon(self, folder, icon):

        mipmap = (
            folder
            / "app"
            / "src"
            / "main"
            / "res"
            / "mipmap"
        )

        mipmap.mkdir(parents=True, exist_ok=True)

        shutil.copy(icon, mipmap / "ic_launcher.png")
