from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PyTodo(QRadioButton):
    _color = QColor('white')

    def __init__(self, task, on_toggle_cb=None, default_val=False):
        super().__init__(task)

        self.on_toggle_cb = on_toggle_cb
        self.setChecked(default_val)

        self.anim = QPropertyAnimation(self, b"color")

        self.opacityEff = QGraphicsOpacityEffect(self)
        self.opacityEff.setOpacity(1)
        self.setGraphicsEffect(self.opacityEff)

        self.setMinimumHeight(20)
        self.setAutoExclusive(False)
        self.toggled.connect(self.on_toggle)
        self.update_stylesheet()

    @Property(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color
        self.update_stylesheet(color=f'rgb({new_color.red()}, {new_color.blue()}, {new_color.green()});')
        self.update()

    def update_stylesheet(self, *args, **kwargs):
        self.setStyleSheet(self.get_stylesheet(*args, **kwargs))

    def get_stylesheet(self, color='white'):
        return f"""
        color: {color};
        font: 10pt \"Segoe UI\";
        """

    def on_toggle(self, val):
        if val:
            self.anim.setEndValue(QColor("#c4c9a5"))
            self.anim.setDuration(100)
            self.anim.start()
            self.opacityEff.setOpacity(.5)
        else:
            self.anim.setEndValue(QColor("white"))
            self.anim.setDuration(100)
            self.anim.start()
            self.opacityEff.setOpacity(1)

        if self.on_toggle_cb:
            self.on_toggle_cb(val)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.toggle()