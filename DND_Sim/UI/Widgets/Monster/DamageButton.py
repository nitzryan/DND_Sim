# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from UI.Widgets.Monster.ui_DamageButton import Ui_DamageButton

STATE_IMMUNE = 0
STATE_RESIST = 1
STATE_NORMAL = 2
STATE_WEAK = 3
STATE_INVALID = 4

class DamageButton(QtWidgets.QWidget):
    def __init__(self, name, buttonState, parent=None):
        super().__init__(parent)
        self.ui = Ui_DamageButton()
        self.ui.setupUi(self)
        self.ui.label.setText(name)
        self.buttonState = buttonState
        self.ui.pushButton.clicked.connect(self.IncrementButton)
        self.SetButtonStyle()

    def IncrementButton(self):
        self.buttonState += 1
        if self.buttonState >= STATE_INVALID:
            self.buttonState = STATE_IMMUNE

        self.SetButtonStyle()


    def SetButtonStyle(self):
        if self.buttonState == STATE_IMMUNE:
            self.ui.pushButton.setStyleSheet('QPushButton {background-color: black}')
            buttonHoverText = "Immune"
            self.ui.pushButton.setToolTip('Immune')
        elif self.buttonState == STATE_RESIST:
            self.ui.pushButton.setStyleSheet('QPushButton {background-color: red}')
            buttonHoverText = "Resist"
            self.ui.pushButton.setToolTip('Resist')
        elif self.buttonState == STATE_NORMAL:
            self.ui.pushButton.setStyleSheet('QPushButton {background-color: yellow}')
            buttonHoverText = "Normal"
            self.ui.pushButton.setToolTip('Normal')
        elif self.buttonState == STATE_WEAK:
            self.ui.pushButton.setStyleSheet('QPushButton {background-color: green}')
            buttonHoverText = "Weak"
            self.ui.pushButton.setToolTip('Weak')
        else:
            self.ui.pushButton.setStyleSheet('QPushButton {background-color: purple}')
            buttonHoverText = "Error"
            self.ui.pushButton.setToolTip('Error State')

        self.ui.pushButton.setToolTip(buttonHoverText)

    def GetButtonState(self):
        return self.buttonState
