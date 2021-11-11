from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .py_todo import PyTodo

class PyDeletableTodo(QHBoxLayout):
    def __init__(
        self,
        task,
        default_val=False,
        on_toggle_cb=None,
        on_delete_cb=None,
        on_rename_cb=None
    ):
        super().__init__()
        self.on_delete_cb = on_delete_cb
        self.on_rename_cb = on_rename_cb

        self.todo = PyTodo(task, on_toggle_cb, default_val)

        self.delete_button = PyTodoButton("src/assets/images/icon_close.svg")
        self.delete_button.clicked.connect(self.on_delete)

        self.rename_button = PyTodoButton("src/assets/images/icon_arrow_left.svg")
        self.rename_button.clicked.connect(self.on_rename)

        self.addWidget(self.todo)
        self.addWidget(self.rename_button)
        self.addWidget(self.delete_button)

        self.delete_button.hide()
        self.rename_button.hide()
        
    def on_delete(self):
        if self.on_delete_cb != None:
            self.on_delete_cb(self)

    def on_rename(self):
        if self.on_rename_cb != None:
            self.on_rename_cb(self)

    def hide(self):
        self.todo.hide()
        self.delete_button.hide()
        self.rename_button.hide()

    def show(self):
        self.todo.show()
        self.delete_button.show()
        self.rename_button.show()



class PyTodoButton(QPushButton):
    def __init__(
        self,
        icon_path
    ):
        super().__init__()


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

        self.setCursor(Qt.PointingHandCursor)
        self.setMaximumSize(30,20)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(10,10))

