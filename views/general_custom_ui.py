from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import *

category_data = {
    "Empezando Tarea",
    "Tarea Finalizada",
    "Tarea en Proceso"
}

class GeneralCustomUi():
    def __init__(self, ui) :
        self.ui = ui

        self.remove_default_title_bar()
        self.ui.top_bar_frame.mouseMoveEvent = self.move_window
        self.set_window_shadow()
        self.ui.pushClose_Button.clicked.connect(self.close_win)
        self.ui.pushMin_Button.clicked.connect(self.minimize_win)
        self.ui.pushMax_Button.clicked.connect(self.mini_maximize)

    def close_win(self):
        self.ui.close()

    def mini_maximize(self):
        if self.ui.isMaximized():
            self.ui.pushMax_Button.setIcon(QIcon("./assets/icons/maximize.svg"))
            self.ui.showNormal()
            self.ui.shadow_layout.setContentsMargins(10, 10, 10, 10)
        else:
            self.ui.pushMax_Button.setIcon(QIcon("./assets/icons/min.svg"))
            self.ui.showMaximized()
            self.ui.shadow_layout.setContentsMargins(0, 0, 0, 0)

    def minimize_win(self):
        self.ui.showMinimized()
        
    def remove_default_title_bar(self):
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)

    def mouse_press_event(self, event):
        self.drag_pos = event.globalPos()

    def move_window(self, event):
        if event.buttons() == Qt.LeftButton:
            self.ui.move(self.ui.pos() + event.globalPos() - self.drag_pos)
            self.drag_pos = event.globalPos()
    
    def set_window_shadow(self):
        shadow = QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#707171")
        self.ui.background_frame.setGraphicsEffect(shadow)

    def fill_category_cb(self):
        self.ui.category_comboBox.addItems(category_data)
