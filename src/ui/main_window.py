from PySide6.QtCore import Qt
# from PySide6.QtGui import *
from PySide6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea, QWidget

from src.widgets.py_button import PyButton
from src.widgets.py_slider import PySlider
from src.widgets.py_toggle import PyToggle
from src.widgets.py_title_bar import PyTitleBar
from src.widgets.py_todo import PyTodo, PyTodoEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(300,200)

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
        self.main_container.layout().setAlignment(Qt.AlignTop)

        self.setCentralWidget(self.main_container)

        # Title Bar
        title_bar_container = QFrame()
        title_bar_container.setMinimumHeight(30)
        title_bar_container.setMaximumHeight(30)
        title_bar_container.setLayout(QVBoxLayout())
        title_bar_container.layout().setContentsMargins(0,0,0,0)

        title_bar = PyTitleBar(self, self)
        title_bar.set_title('QuteTodo - The Best Todo List')
        title_bar.add_todo_button.clicked.connect(self.add_todo)
        title_bar_container.layout().addWidget(title_bar)

        self.main_container.layout().addWidget(title_bar_container)


        # Todo Container
        todo_scroll_container = QScrollArea()
        todo_scroll_container.setWidgetResizable(True)
        todo_scroll_container.setStyleSheet('background: transparent;')
        todo_scroll_container.setFrameShape(QFrame.NoFrame)
        todo_scroll_container.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        todo_scroll_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_container.layout().addWidget(todo_scroll_container)

        self.todo_container = QWidget()
        self.todo_container.setLayout(QVBoxLayout())
        todo_scroll_container.setWidget(self.todo_container)

        # Todos
        todo1 = PyTodo("Clean The Dog")
        todo2 = PyTodo("Clean The Cat")
        for td in [todo1, todo2]:
            self.todo_container.layout().addWidget(td)
        
        self.show()

    def add_todo(self):
        count = self.todo_container.layout().count()

        def create_todo_from_todoedit(todoedit):
            todoedit.setParent(None)
            self.todo_container.layout().insertWidget(count, PyTodo(todoedit.text()))

        new_todo_edit = PyTodoEdit(create_todo_from_todoedit)
        self.todo_container.layout().addWidget(new_todo_edit)
        new_todo_edit.setFocus()



    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()
