from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class PyTodoEdit(QLineEdit):
    def __init__(self, cb):
        super().__init__()

        self.cb = cb

        self.setStyleSheet("""
        QLineEdit {
            border: 3px solid #1E1E1E;
            border-radius: 10px;
            background-color: #1E1E1E;
            color: white;
        }
        """)

        self.editingFinished.connect(self.edit_finished)

    def edit_finished(self):
        self.cb(self)

