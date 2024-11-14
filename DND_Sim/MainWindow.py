# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from UI.Widgets.Sidebar import Sidebar
from UI.Pages.Monster import Monster

import requests

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sidebar = Sidebar()
        self.ui.sidebarLayout.addWidget(self.sidebar)

        response = requests.get("https://www.dnd5eapi.co/api/monsters/acolyte")
        data = response.json()
        self.monsterPage = Monster(data)
        self.ui.mainLayout.addWidget(self.monsterPage)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
