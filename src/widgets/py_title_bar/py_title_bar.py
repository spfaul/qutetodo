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
from PySide6.QtSvgWidgets import *

import os

# IMPORT DIV
# ///////////////////////////////////////////////////////////////
from . py_div import PyDiv

# IMPORT BUTTON
# ///////////////////////////////////////////////////////////////
from . py_title_button import PyTitleButton

# GLOBALS
# ///////////////////////////////////////////////////////////////

# HELPER FUNCTIONS
def set_svg_icon(icon_name):
    app_path = os.path.abspath(os.getcwd())
    folder = "src/assets/images"
    path = os.path.join(app_path, folder)
    icon = os.path.normpath(os.path.join(path, icon_name))
    return icon

# SET SVG IMAGE
# ///////////////////////////////////////////////////////////////
def set_svg_image(icon_name):
    app_path = os.path.abspath(os.getcwd())
    folder = "src/assets/images"
    path = os.path.join(app_path, folder)
    icon = os.path.normpath(os.path.join(path, icon_name))
    return icon

# SET IMAGE
# ///////////////////////////////////////////////////////////////
def set_image(image_name):
    app_path = os.path.abspath(os.getcwd())
    folder = "src/assets/images"
    path = os.path.join(app_path, folder)
    image = os.path.normpath(os.path.join(path, image_name))
    return image

# PY TITLE BAR
# Top bar with move application, maximize, restore, minimize,
# close buttons and extra buttons
# ///////////////////////////////////////////////////////////////
class PyTitleBar(QWidget):
    # SIGNALS
    clicked = Signal(object)
    released = Signal(object)

    def __init__(
        self,
        parent,
        app_parent,
        logo_image = "logo_top_100x22.svg",
        logo_width = 100,
        buttons = None,
        dark_one = "#1b1e23",
        bg_color = "#343b48",
        div_color = "#3c4454",
        btn_bg_color = "#343b48",
        btn_bg_color_hover = "#3c4454",
        btn_bg_color_pressed = "#2c313c",
        icon_color = "#c3ccdf",
        icon_color_hover = "#dce1ec",
        icon_color_pressed = "#edf0f5",
        icon_color_active = "#f5f6f9",
        context_color = "#6c99f4",
        text_foreground = "#8a95aa",
        radius = 8,
        font_family = "Segoe UI",
        title_size = 10,
        is_custom_title_bar = True,
    ):
        super().__init__()


        # PARAMETERS
        self._logo_image = logo_image
        self._dark_one = dark_one
        self._bg_color = bg_color
        self._div_color = div_color
        self._parent = parent
        self._app_parent = app_parent
        self._btn_bg_color = btn_bg_color
        self._btn_bg_color_hover = btn_bg_color_hover
        self._btn_bg_color_pressed = btn_bg_color_pressed  
        self._context_color = context_color
        self._icon_color = icon_color
        self._icon_color_hover = icon_color_hover
        self._icon_color_pressed = icon_color_pressed
        self._icon_color_active = icon_color_active
        self._font_family = font_family
        self._title_size = title_size
        self._text_foreground = text_foreground
        self._is_custom_title_bar = is_custom_title_bar

        # SETUP UI
        self.setup_ui()

        # ADD BG COLOR
        self.bg.setStyleSheet(f"background-color: {bg_color}; border-radius: {radius}px;")

        # SET LOGO AND WIDTH
        self.top_logo.setMinimumWidth(logo_width)
        self.top_logo.setMaximumWidth(logo_width)
        #self.top_logo.setPixmap(set_svg_image(logo_image))

        # MOVE WINDOW / MAXIMIZE / RESTORE
        # ///////////////////////////////////////////////////////////////
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                parent.move(parent.pos() + event.globalPos() - parent.dragPos)
                parent.dragPos = event.globalPos()
                event.accept()

        # MOVE APP WIDGETS
        if is_custom_title_bar:
            self.top_logo.mouseMoveEvent = moveWindow
            self.div_1.mouseMoveEvent = moveWindow
            self.title_label.mouseMoveEvent = moveWindow
            self.div_2.mouseMoveEvent = moveWindow
            self.div_3.mouseMoveEvent = moveWindow


        # ADD WIDGETS TO TITLE BAR
        # ///////////////////////////////////////////////////////////////
        self.bg_layout.addWidget(self.top_logo)
        self.bg_layout.addWidget(self.div_1)
        self.bg_layout.addWidget(self.title_label)
        self.bg_layout.addWidget(self.div_2)

        # ADD BUTTONS BUTTONS
        # ///////////////////////////////////////////////////////////////
        self.close_button.released.connect(lambda: parent.close())

        # Extra BTNs layout
        self.bg_layout.addLayout(self.custom_buttons_layout)

        # ADD Buttons
        if is_custom_title_bar:            
            self.bg_layout.addWidget(self.add_todo_button)
            self.bg_layout.addWidget(self.close_button)

    # ADD BUTTONS TO TITLE BAR
    # Add btns and emit signals
    # ///////////////////////////////////////////////////////////////
    def add_menus(self, parameters):
        if parameters != None and len(parameters) > 0:
            for parameter in parameters:
                _btn_icon = set_svg_icon(parameter['btn_icon'])
                _btn_id = parameter['btn_id']
                _btn_tooltip = parameter['btn_tooltip']
                _is_active = parameter['is_active']

                self.menu = PyTitleButton(
                    self._parent,
                    self._app_parent,
                    btn_id = _btn_id,
                    tooltip_text = _btn_tooltip,
                    dark_one = self._dark_one,
                    bg_color = self._bg_color,
                    bg_color_hover = self._btn_bg_color_hover,
                    bg_color_pressed = self._btn_bg_color_pressed,
                    icon_color = self._icon_color,
                    icon_color_hover = self._icon_color_active,
                    icon_color_pressed = self._icon_color_pressed,
                    icon_color_active = self._icon_color_active,
                    context_color = self._context_color,
                    text_foreground = self._text_foreground,
                    icon_path = _btn_icon,
                    is_active = _is_active
                )
                self.menu.clicked.connect(self.btn_clicked)
                self.menu.released.connect(self.btn_released)

                # ADD TO LAYOUT
                self.custom_buttons_layout.addWidget(self.menu)

            # ADD DIV
            if self._is_custom_title_bar:
                self.custom_buttons_layout.addWidget(self.div_3)

    # TITLE BAR MENU EMIT SIGNALS
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        self.clicked.emit(self.menu)
    
    def btn_released(self):
        self.released.emit(self.menu)

    # SET TITLE BAR TEXT
    # ///////////////////////////////////////////////////////////////
    def set_title(self, title):
        self.title_label.setText(title)



    # SETUP APP
    # ///////////////////////////////////////////////////////////////
    def setup_ui(self):
        # ADD MENU LAYOUT
        self.title_bar_layout = QVBoxLayout(self)
        self.title_bar_layout.setContentsMargins(0,0,0,0)

        # ADD BG
        self.bg = QFrame()

        # ADD BG LAYOUT
        self.bg_layout = QHBoxLayout(self.bg)
        self.bg_layout.setContentsMargins(10,0,5,0)
        self.bg_layout.setSpacing(0)

        # DIVS
        self.div_1 = PyDiv(self._div_color)
        self.div_2 = PyDiv(self._div_color)
        self.div_3 = PyDiv(self._div_color)

        # LEFT FRAME WITH MOVE APP
        self.top_logo = QLabel()
        self.top_logo_layout = QVBoxLayout(self.top_logo)
        self.top_logo_layout.setContentsMargins(0,0,0,0)
        self.logo_svg = QSvgWidget()
        self.logo_svg.load(set_svg_image(self._logo_image))
        self.top_logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # TITLE LABEL
        self.title_label = QLabel()
        self.title_label.setAlignment(Qt.AlignVCenter)
        self.title_label.setStyleSheet(f"""
            font: {self._title_size}pt \"{self._font_family}\";
            color: white;

        """)

        # CUSTOM BUTTONS LAYOUT
        self.custom_buttons_layout = QHBoxLayout()
        self.custom_buttons_layout.setContentsMargins(0,0,0,0)
        self.custom_buttons_layout.setSpacing(3)

        self.add_todo_button = PyTitleButton(
            self._parent,
            self._app_parent,
            tooltip_text = "Add Todo",
            dark_one = self._dark_one,
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._btn_bg_color_pressed,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_pressed,
            icon_color_active = self._icon_color_active,
            context_color = self._context_color,
            text_foreground = self._text_foreground,
            radius = 6,
            icon_path = set_svg_icon("icon_minimize.svg")
        )


        # CLOSE BUTTON
        self.close_button = PyTitleButton(
            self._parent,
            self._app_parent,
            tooltip_text = "Close app",
            dark_one = self._dark_one,
            bg_color = self._btn_bg_color,
            bg_color_hover = self._btn_bg_color_hover,
            bg_color_pressed = self._context_color,
            icon_color = self._icon_color,
            icon_color_hover = self._icon_color_hover,
            icon_color_pressed = self._icon_color_active,
            icon_color_active = self._icon_color_active,
            context_color = self._context_color,
            text_foreground = self._text_foreground,
            radius = 6,
            icon_path = set_svg_icon("icon_close.svg")
        )

        # ADD TO LAYOUT
        self.title_bar_layout.addWidget(self.bg)