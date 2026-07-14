"""
Shiny Website To APK Converter
Main entry point.

Author: Shiny Studios
License: MIT
"""

import sys
from PySide6.QtWidgets import QApplication
from gui import MainWindow


def main():
    """Start the application."""

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
