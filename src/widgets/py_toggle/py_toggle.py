# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class PyToggle(QCheckBox):
    def __init__(
        self,
        width = 50,
        height = 28,
        circle_margin = 4,
        bg_color = "#777", 
        circle_color = "#DDD",
        active_color = "#00BCFF",
        animation_curve = QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self)
        self.setFixedSize(width, height)
        self.setCursor(Qt.PointingHandCursor)

        # COLORS
        self._bg_color = bg_color
        self._circle_color = circle_color
        self._active_color = active_color

        self._circle_margin = circle_margin

        self._position = self._start_position = 4
        self.animation = QPropertyAnimation(self, b"position")
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)
        self.stateChanged.connect(self.setup_animation)

    @Property(float)
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = pos
        self.update()

    # START STOP ANIMATION
    def setup_animation(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(self.width() - self.height()+self._circle_margin - self._start_position+2 )
        else:
            self.animation.setEndValue(self._start_position)
        self.animation.start()
    
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setFont(QFont("Segoe UI", 9))

        # SET PEN
        p.setPen(Qt.NoPen)

        # DRAW RECT
        rect = QRect(0, 0, self.width(), self.height())        

        if not self.isChecked():
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(0,0,rect.width(), rect.height(), rect.height()/2, rect.height()/2)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, self._circle_margin, rect.height()-self._circle_margin*2, rect.height()-self._circle_margin*2)
        else:
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(0,0,rect.width(), rect.height(), rect.height()/2, rect.height()/2)
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse(self._position, self._circle_margin, rect.height()-self._circle_margin*2, rect.height()-self._circle_margin*2)

        p.end()