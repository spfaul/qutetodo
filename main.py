import sys
from PySide6.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.core.config import get_config


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(get_config())
    sys.exit(app.exec_())

