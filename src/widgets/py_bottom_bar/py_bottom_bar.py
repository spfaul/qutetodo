from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PyBottomBar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)

        self.container = QFrame()
        self.container.setStyleSheet("""
            background-color: #343b48;
            border-radius: 5px;
        """)
        self.container_layout = QHBoxLayout(self.container)
        self.container_layout.setContentsMargins(0,0,0,0)

        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet("""
        QProgressBar {
            text-align: center;
            border-radius: 10px;
            border-style: none;
            background-color: rgb(98,114,164);
            color: rgb(255, 255, 255);
        }

        QProgressBar::chunk {
            border-radius: 10px;
            border-style: none;
            background-color: qlineargradient(spread:pad, x1:0, y1:0.483, x2:1, y2:0.5, stop:0 rgba(220, 96, 220, 255), stop:1 rgba(170, 85, 255, 255));
        }
        """)
        self.progress_bar.setMaximumHeight(20)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(2)
        self.container_layout.addWidget(self.progress_bar)

        self.layout.addWidget(self.container)

