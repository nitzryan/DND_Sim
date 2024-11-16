# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from UI.Pages.ui_Monster import Ui_Monster
from UI.Widgets.Monster.MonsterMovement import MonsterMovement
from UI.Widgets.Monster.DamageButton import DamageButton, STATE_IMMUNE, STATE_RESIST, STATE_NORMAL, STATE_WEAK

class Monster(QtWidgets.QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.ui = Ui_Monster()
        self.ui.setupUi(self)
        if data is not None:
            self.SetMonster(data)

    def SetMonster(self, data):
        # Stats
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

        # Movement
        movementWidget = QtWidgets.QWidget()
        self.ui.saMovement.setWidget(movementWidget)
        movementLayout = QtWidgets.QVBoxLayout(movementWidget)
        for type, speed in data["speed"].items():
            mm = MonsterMovement(type, speed)
            movementLayout.addWidget(mm)

        # Damage Types
        self.acidType = DamageButton("Acid", GetState(data, "acid"))
        self.ui.damageTypesLayout.addWidget(self.acidType)
        self.bludgType = DamageButton("Bludg", GetState(data, "bludgeoning"))
        self.ui.damageTypesLayout.addWidget(self.bludgType)
        self.coldType = DamageButton("Cold", GetState(data, "cold"))
        self.ui.damageTypesLayout.addWidget(self.coldType)
        self.fireType = DamageButton("Fire", GetState(data, "fire"))
        self.ui.damageTypesLayout.addWidget(self.fireType)
        self.forceType = DamageButton("Force", GetState(data, "force"))
        self.ui.damageTypesLayout.addWidget(self.forceType)
        self.lightningType = DamageButton("Lightning", GetState(data, "lightning"))
        self.ui.damageTypesLayout.addWidget(self.lightningType)
        self.necroticType = DamageButton("Necrotic", GetState(data, "necrotic"))
        self.ui.damageTypesLayout.addWidget(self.necroticType)
        self.piercingType = DamageButton("Piercing", GetState(data, "piercing"))
        self.ui.damageTypesLayout.addWidget(self.piercingType)
        self.poisonType = DamageButton("Poison", GetState(data, "poison"))
        self.ui.damageTypesLayout.addWidget(self.poisonType)
        self.psychicType = DamageButton("Psychic", GetState(data, "psychic"))
        self.ui.damageTypesLayout.addWidget(self.psychicType)
        self.radiantType = DamageButton("Radiant", GetState(data, "radiant"))
        self.ui.damageTypesLayout.addWidget(self.radiantType)
        self.slashingType = DamageButton("Slashing", GetState(data, "slashing"))
        self.ui.damageTypesLayout.addWidget(self.slashingType)
        self.thunderType = DamageButton("Thunder", GetState(data, "thunder"))
        self.ui.damageTypesLayout.addWidget(self.thunderType)

def GetState(data, type):
    if type in data["damage_vulnerabilities"]:
        return STATE_WEAK
    if type in data["damage_resistances"]:
        return STATE_RESIST
    if type in data["damage_immunities"]:
        return STATE_IMMUNE
    return STATE_NORMAL
