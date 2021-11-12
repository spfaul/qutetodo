from PySide6.QtCore import Qt, QTimer, QEvent
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QScrollArea, QWidget
from configparser import SectionProxy
from typing import NoReturn, List

from src.core.autosave import AutoSave, TodoInfo
from src.widgets.py_button import PyButton
from src.widgets.py_slider import PySlider
from src.widgets.py_toggle import PyToggle
from src.widgets.py_title_bar import PyTitleBar
from src.widgets.py_todo import PyDeletableTodo, PyTodoEdit, PyTodo
from src.widgets.py_bottom_bar import PyBottomBar
from src.widgets.py_grips import PyGrips

class MainWindow(QMainWindow):
    def __init__(self, config: SectionProxy):
        super(MainWindow, self).__init__()

        self.config: SectionProxy = config

        self.do_save: bool = self.config.getboolean('DoAutoSave')
        if self.do_save:
            self.saver: AutoSave = AutoSave(self.config.get('SaveFile'))

        self.edit_mode: bool = False
        self.todos_done: int = 0

        if self.config.getboolean('WindowStayOnTop'):
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(float(self.config.get('Opacity')))
        self.resize(int(self.config.get('StartupHeight')), int(self.config.get('StartupWidth')))

        self.setup_ui()

        self.show()

    def setup_ui(self) -> NoReturn:
        self.main_container: QFrame = QFrame(self)
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
        title_bar_container: QFrame = QFrame()
        title_bar_container.setMinimumHeight(30)
        title_bar_container.setMaximumHeight(30)
        title_bar_container.setLayout(QVBoxLayout())
        title_bar_container.layout().setContentsMargins(0,0,0,0)

        self.title_bar: PyTitleBar = PyTitleBar(self, self)
        self.title_bar.set_title(self.config.get('Title'))
        
        self.title_bar.add_todo_button.clicked.connect(self.add_todo)
        self.title_bar.toggle_edit_button.clicked.connect(self.toggle_edit_mode)

        title_bar_container.layout().addWidget(self.title_bar)
        self.main_container.layout().addWidget(title_bar_container)

        # Todo Container
        self.todo_scroll_container: QScrollArea = QScrollArea()
        self.todo_scroll_container.setWidgetResizable(True)
        self.todo_scroll_container.setStyleSheet('background: transparent;')
        self.todo_scroll_container.setFrameShape(QFrame.NoFrame)
        self.todo_scroll_container.verticalScrollBar().setStyleSheet("""
            QScrollBar:vertical {
                background-color: #495367;
                width: 12px;
                border-radius: 5px;
            }

            QScrollBar::handle:vertical {
                background-color: #7a7f84;
                min-height: 10px;
                border-radius: 5px;
            }

            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }

            QScrollBar::add-line {
                border: none;
                background: none;
            }

            QScrollBar::sub-line {
                border: none;
                background: none;
            }
        """)
        self.todo_scroll_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_container.layout().addWidget(self.todo_scroll_container)

        self.todo_container: QWidget = QWidget()
        self.todo_container.setLayout(QVBoxLayout())
        self.todo_scroll_container.setWidget(self.todo_container)

        # Load Todos
        if self.do_save:
             todo_infos: TodoInfo = self.saver.load()

             for todo in todo_infos:
                self.todo_container.layout().addLayout(
                    PyDeletableTodo(
                        todo['description'],
                        default_val=todo['complete'],
                        on_toggle_cb=self.on_todo_toggle,
                        on_delete_cb=self.delete_todo,
                        on_rename_cb=self.edit_todo
                        )
                )
                if todo['complete']:
                    self.todos_done += 1

        # Bottom Bar
        self.bott_bar: PyBottomBar = PyBottomBar()
        self.bott_bar.setFocusPolicy(Qt.NoFocus)
        self.main_container.layout().addWidget(self.bott_bar)

        self.update_prog_bar()

        self.left_grip: PyGrips = PyGrips(self, "left")
        self.right_grip: PyGrips = PyGrips(self, "right")
        self.top_grip: PyGrips = PyGrips(self, "top")
        self.bottom_grip: PyGrips = PyGrips(self, "bottom")
        self.top_left_grip: PyGrips = PyGrips(self, "top_left")
        self.top_right_grip: PyGrips = PyGrips(self, "top_right")
        self.bottom_left_grip: PyGrips = PyGrips(self, "bottom_left")
        self.bottom_right_grip: PyGrips = PyGrips(self, "bottom_right")

    def resizeEvent(self, event: QResizeEvent) -> NoReturn:
        self.left_grip.setGeometry(5, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
        self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
        self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
        self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
        self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
        self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    def update_save_file(self) -> NoReturn:
        count: int = self.todo_container.layout().count()
        todos: List[PyTodo] = []
        for i in range(count):
            todos.append(self.todo_container.layout().itemAt(i).todo)
        self.saver.save(todos)

    def add_todo(self) -> NoReturn:
        self.title_bar.add_todo_button.setEnabled(False)
        self.title_bar.toggle_edit_button.setEnabled(False)
        count: int = self.todo_container.layout().count()

        def create_todo_from_todoedit(todoedit: PyTodoEdit) -> NoReturn:
            self.title_bar.add_todo_button.setEnabled(True)
            self.title_bar.toggle_edit_button.setEnabled(True)

            todoedit.setParent(None)
            todo: PyDeletableTodo = PyDeletableTodo(
                todoedit.text(), 
                on_toggle_cb=self.on_todo_toggle,
                on_delete_cb=self.delete_todo,
                on_rename_cb=self.edit_todo
            )
            self.todo_container.layout().insertLayout(count, todo)
            self.update_prog_bar()
            if self.do_save:
                self.update_save_file()

        new_todo_edit: PyTodoEdit = PyTodoEdit(create_todo_from_todoedit)
        self.todo_container.layout().addWidget(new_todo_edit)

        new_todo_edit.setFocus()
        QTimer.singleShot(5, self.scroll_to_bottom)

    def on_todo_toggle(self, val) -> NoReturn:
        if val:
            self.todos_done += 1
        else:
            self.todos_done -= 1
        self.bott_bar.progress_bar.setValue(self.todos_done)

        if self.do_save:
            self.update_save_file()

    def scroll_to_bottom(self) -> NoReturn:
        self.todo_scroll_container.ensureVisible(0, self.todo_container.height())

    def mousePressEvent(self, event: QMouseEvent) -> NoReturn:
        print(type(event))
        self.dragPos = event.globalPos()

    def toggle_edit_mode(self) -> NoReturn:
        self.edit_mode = not self.edit_mode

        self.title_bar.add_todo_button.setEnabled(not self.edit_mode)
        
        count: int = self.todo_container.layout().count()
        for i in range(count):
            todo: PyDeletableTodo = self.todo_container.layout().itemAt(i)

            if self.edit_mode:
                todo.delete_button.show()
                todo.rename_button.show()
            else:
                todo.rename_button.hide()
                todo.delete_button.hide()

    def delete_todo(self, todo: PyDeletableTodo) -> NoReturn:
        todo.hide()
        todo.setParent(None)
        self.on_todo_toggle(False)
        self.update_prog_bar()

        if self.do_save:
            self.update_save_file()

    def edit_todo(self, todo: PyDeletableTodo) -> NoReturn:
        self.title_bar.toggle_edit_button.setEnabled(False)
        
        def finish_edit(todoedit: PyTodoEdit) -> NoReturn:
            todoedit.setParent(None)
            todo.todo.setText(todoedit.text())
            todo.show()
            self.title_bar.toggle_edit_button.setEnabled(True)
            
            if self.do_save:
                self.update_save_file()

        todo.hide()
        todoedit: PyTodoEdit = PyTodoEdit(finish_edit)
        todoedit.setText(todo.todo.text())
        todo.addWidget(todoedit)
        todoedit.setFocus()

    def update_prog_bar(self) -> NoReturn:
        self.bott_bar.progress_bar.setValue(self.todos_done)
        
        item_count: int = self.todo_container.layout().count()
        if item_count == 0:
            self.bott_bar.progress_bar.setMaximum(1)
        else:
            self.bott_bar.progress_bar.setMaximum(item_count)

