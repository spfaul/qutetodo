from PySide6.QtCore import Qt, QTimer
# from PySide6.QtGui import *
from PySide6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea, QWidget

import time

from src.widgets.py_button import PyButton
from src.widgets.py_slider import PySlider
from src.widgets.py_toggle import PyToggle
from src.widgets.py_title_bar import PyTitleBar
from src.widgets.py_todo import PyTodo, PyTodoEdit
from src.widgets.py_bottom_bar import PyBottomBar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(.8)
        self.resize(300,300)

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
        self.main_container.layout().setAlignment(Qt.AlignVCenter)

        self.setCentralWidget(self.main_container)

        # Title Bar
        title_bar_container = QFrame()
        title_bar_container.setMinimumHeight(30)
        title_bar_container.setMaximumHeight(30)
        title_bar_container.setLayout(QVBoxLayout())
        title_bar_container.layout().setContentsMargins(0,0,0,0)

        title_bar = PyTitleBar(self, self)
        title_bar.set_title('QuteTodo - Minimalist Todo List')
        title_bar.add_todo_button.clicked.connect(self.add_todo)
        title_bar_container.layout().addWidget(title_bar)

        self.main_container.layout().addWidget(title_bar_container)

        # Todo Container
        self.todo_scroll_container = QScrollArea()
        self.todo_scroll_container.setWidgetResizable(True)
        self.todo_scroll_container.setStyleSheet('background: transparent;')
        self.todo_scroll_container.setFrameShape(QFrame.NoFrame)
        # self.todo_scroll_container.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.todo_scroll_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_container.layout().addWidget(self.todo_scroll_container)

        self.todo_container = QWidget()
        self.todo_container.setLayout(QVBoxLayout())
        self.todo_scroll_container.setWidget(self.todo_container)

        # Todos
        self.todos_done = 0
        todo1 = PyTodo("Clean The Dog", self.on_todo_toggle)
        todo2 = PyTodo("Clean The Cat", self.on_todo_toggle)
        for td in [todo1, todo2]:
            self.todo_container.layout().addWidget(td)
        
        # Bottom Bar
        self.bott_bar = PyBottomBar()
        self.main_container.layout().addWidget(self.bott_bar)

        self.show()

    def add_todo(self):
        count = self.todo_container.layout().count()
        def create_todo_from_todoedit(todoedit):
            todoedit.setParent(None)
            self.todo_container.layout().insertWidget(count, PyTodo(todoedit.text(), self.on_todo_toggle))
            self.bott_bar.progress_bar.setMaximum(self.todo_container.layout().count())

        new_todo_edit = PyTodoEdit(create_todo_from_todoedit)
        self.todo_container.layout().addWidget(new_todo_edit)
        new_todo_edit.setFocus()
        QTimer.singleShot(5, self.scroll_to_bottom)

    def on_todo_toggle(self, val):
        if val:
            self.todos_done += 1
        else:
            self.todos_done -= 1
        self.bott_bar.progress_bar.setValue(self.todos_done)

    def scroll_to_bottom(self):
        self.todo_scroll_container.ensureVisible(0, self.todo_container.height())

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
