import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.ui.main_window import MainWindow
from src.core.config import get_config


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    window: QMainWindow = MainWindow(get_config())
    sys.exit(app.exec_())

