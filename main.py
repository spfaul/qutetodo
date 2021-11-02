import sys
from PySide6.QtWidgets import QApplication
from src.ui.main_window import MainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

