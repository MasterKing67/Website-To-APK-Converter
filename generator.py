import os
import shutil

TEXT_EXTENSIONS = (
    ".java",
    ".xml",
    ".gradle",
    ".kts",
    ".properties",
    ".txt",
    ".md",
)

ORIGINAL_PACKAGE = "com.shiny.calculator"


def replace_in_file(file_path, replacements):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        for old, new in replacements.items():
            content = content.replace(old, new)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    except Exception:
        pass


def generate_project(app_name, package_name, website_url, output_folder):
    template = "android_template"

    project_folder = os.path.join(output_folder, app_name)

    if os.path.exists(project_folder):
        shutil.rmtree(project_folder)

    shutil.copytree(template, project_folder)

    replacements = {
        "{APP_NAME}": app_name,
        "{PACKAGE_NAME}": package_name,
        "{WEBSITE_URL}": website_url,
        ORIGINAL_PACKAGE: package_name,
    }

    for root, dirs, files in os.walk(project_folder):
        for file in files:
            if file.endswith(TEXT_EXTENSIONS):
                replace_in_file(
                    os.path.join(root, file),
                    replacements
                )

    old_package = ORIGINAL_PACKAGE.split(".")
    new_package = package_name.split(".")

    old_path = os.path.join(
        project_folder,
        "app",
        "src",
        "main",
        "java",
        *old_package
    )

    if os.path.exists(old_path):
        java_root = os.path.join(
            project_folder,
            "app",
            "src",
            "main",
            "java"
        )

        new_path = os.path.join(java_root, *new_package)

        os.makedirs(os.path.dirname(new_path), exist_ok=True)

        shutil.move(old_path, new_path)

        # Remove empty old folders
        current = os.path.dirname(old_path)

        while current.startswith(java_root):
            try:
                os.rmdir(current)
            except OSError:
                break
            current = os.path.dirname(current)

    return project_folder
