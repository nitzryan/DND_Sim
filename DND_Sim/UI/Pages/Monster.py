# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from UI.Pages.ui_Monster import Ui_Monster


class Monster(QtWidgets.QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.ui = Ui_Monster()
        self.ui.setupUi(self)
        if data is not None:
            self.SetMonster(data)

    def SetMonster(self, data):
        self.ui.name.setText(data["name"])
        self.ui.sbAC.setValue(data["armor_class"][0]["value"])
        self.ui.sbHP.setValue(data["hit_points"])
        self.ui.sbStr.setValue(data["strength"])
        self.ui.sbDex.setValue(data["dexterity"])
        self.ui.sbCon.setValue(data["constitution"])
        self.ui.sbInt.setValue(data["intelligence"])
        self.ui.sbWis.setValue(data["wisdom"])
        self.ui.sbCha.setValue(data["charisma"])
        self.ui.sbProf.setValue(data["proficiency_bonus"])
        self.ui.sbXP.setValue(data["xp"])
        self.ui.cbType.setCurrentText(data["type"].capitalize())
        self.ui.cbSize.setCurrentText(data["size"].capitalize())
