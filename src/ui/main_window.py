from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout
import sys

from src.widgets.py_button import PyButton
from src.widgets.py_slider import PySlider
from src.widgets.py_toggle import PyToggle
from src.widgets.py_title_bar import PyTitleBar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.main_container = QFrame(self)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet("""
        #main_container {
            background-color: #2c313c;
            border-radius: 10;
            border: 2px solid #343b48;
        }
        """)
        self.main_container.setLayout(QVBoxLayout())

        self.setCentralWidget(self.main_container)


        # Title Bar
        title_bar_container = QFrame()
        title_bar_container.setMinimumHeight(30)
        title_bar_container.setMaximumHeight(30)
        title_bar_container.setLayout(QVBoxLayout())
        title_bar_container.layout().setContentsMargins(0,0,0,0)

        title_bar = PyTitleBar(self, self)
        title_bar.set_title('QuteTodo - The Best Todo List')
        title_bar_container.layout().addWidget(title_bar)
        self.main_container.layout().addWidget(title_bar_container)

        # Widgets
        self.btn_1 = PyButton("Test!")
        self.btn_2 = PyButton("Woohoo!")

        self.slider = PySlider()
        self.slider.setMinimum(70)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(1)
        self.slider.setValue(80)
        self.on_slider_changed()

        self.workspace_container = QHBoxLayout()
        self.workspace_container.addWidget(self.btn_1)
        self.workspace_container.addWidget(self.btn_2)
        self.workspace_container.addWidget(self.slider)
        self.workspace_container.addWidget(PyToggle(width=40, height=20, circle_margin=3, active_color="#0379FF"))
        self.main_container.layout().addLayout(self.workspace_container)

        # Signals
        self.slider.valueChanged.connect(self.on_slider_changed)

        self.resize(300,200)
        self.show()

    def on_slider_changed(self):
        val = self.slider.value()
        self.setWindowOpacity(val/100)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
