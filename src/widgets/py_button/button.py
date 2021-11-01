from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class PyButton(QPushButton):
    def __init__(self, *args):
        super().__init__(*args)


        self.setStyleSheet(u"""
        QPushButton {
            background-color: #1b1e23;
            border-radius: 5;
            border: 3px solid #1b1e23;
            color: white;
        }

        QPushButton:hover {
            background-color: #262c30;
            border-color: #262c30;
        }

        QPushButton:pressed {
            background-color: #4c565b;
            border-color: #4c565b;
        }
        """)







