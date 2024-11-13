# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets

from UI.Widgets.ui_Sidebar import Ui_Sidebar

class Sidebar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Sidebar()
        self.ui.setupUi(self)
