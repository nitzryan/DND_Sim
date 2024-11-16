# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from UI.Widgets.Monster.ui_MonsterMovement import Ui_MonsterMovement

class MonsterMovement(QtWidgets.QWidget):
    def __init__(self, name, value, parent=None):
        super().__init__(parent)
        self.ui = Ui_MonsterMovement()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText(name)
        intValue = int(value.split(" ")[0])
        self.ui.spinBox.setValue(intValue)
        self.ui.pushButton.clicked.connect(self.delete)

    def GetName(self):
        return self.ui.label.text()

    def GetValue(self):
        return self.ui.spinBox.value()

    def delete(self):
        self.deleteLater()
