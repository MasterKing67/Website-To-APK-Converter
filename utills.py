"""
utils.py

Utility functions for
Shiny Website To APK Converter

Author: Shiny Studios
"""

from pathlib import Path
import shutil


def create_folder(path):
    """Create a folder if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def copy_file(source, destination):
    """Copy a single file."""
    shutil.copy2(source, destination)


def copy_folder(source, destination):
    """Copy an entire folder."""
    shutil.copytree(source, destination, dirs_exist_ok=True)


def delete_folder(path):
    """Delete a folder if it exists."""
    folder = Path(path)

    if folder.exists():
        shutil.rmtree(folder)


def replace_in_file(file_path, replacements):
    """
    Replace placeholders inside a text file.

    replacements example:
    {
        "{APP_NAME}": "My App",
        "{PACKAGE_NAME}": "com.example.app"
    }
    """

    file = Path(file_path)

    text = file.read_text(encoding="utf-8")

    for old, new in replacements.items():
        text = text.replace(old, new)

    file.write_text(text, encoding="utf-8")


def get_all_files(folder):
    """Return all files inside a folder."""
    return list(Path(folder).rglob("*"))


def is_image(file_path):
    """Check if a file is a supported image."""

    extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".ico",
        ".webp",
    )

    return Path(file_path).suffix.lower() in extensions


def project_exists(output_folder, app_name):
    """Check if the project already exists."""

    project = Path(output_folder) / app_name

    return project.exists()
