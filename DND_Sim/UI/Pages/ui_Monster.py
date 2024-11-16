# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Monster.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Monster(object):
    def setupUi(self, Monster):
        if not Monster.objectName():
            Monster.setObjectName(u"Monster")
        Monster.resize(1250, 860)
        Monster.setStyleSheet(u"QLineEdit {\n"
"	background: transparent;\n"
"}\n"
"\n"
"QComboBox {\n"
"	text-align: center;\n"
"}")
        self.verticalLayout = QVBoxLayout(Monster)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.overviewLayout = QVBoxLayout()
        self.overviewLayout.setObjectName(u"overviewLayout")
        self.name = QLineEdit(Monster)
        self.name.setObjectName(u"name")
        font = QFont()
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setAlignment(Qt.AlignCenter)

        self.overviewLayout.addWidget(self.name)

        self.cbType = QComboBox(Monster)
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.setObjectName(u"cbType")
        font1 = QFont()
        font1.setPointSize(12)
        self.cbType.setFont(font1)

        self.overviewLayout.addWidget(self.cbType)

        self.pbRace = QPushButton(Monster)
        self.pbRace.setObjectName(u"pbRace")
        self.pbRace.setFont(font1)

        self.overviewLayout.addWidget(self.pbRace)

        self.cbSize = QComboBox(Monster)
        self.cbSize.addItem("")
        self.cbSize.addItem("")
        self.cbSize.addItem("")
        self.cbSize.addItem("")
        self.cbSize.addItem("")
        self.cbSize.addItem("")
        self.cbSize.setObjectName(u"cbSize")
        self.cbSize.setFont(font1)

        self.overviewLayout.addWidget(self.cbSize)


        self.verticalLayout.addLayout(self.overviewLayout)

        self.editorLayout = QHBoxLayout()
        self.editorLayout.setObjectName(u"editorLayout")
        self.statsLayout = QVBoxLayout()
        self.statsLayout.setObjectName(u"statsLayout")
        self.hpLayout = QHBoxLayout()
        self.hpLayout.setObjectName(u"hpLayout")
        self.label = QLabel(Monster)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.hpLayout.addWidget(self.label)

        self.sbHP = QSpinBox(Monster)
        self.sbHP.setObjectName(u"sbHP")
        self.sbHP.setFont(font1)
        self.sbHP.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbHP.setMaximum(9999)

        self.hpLayout.addWidget(self.sbHP)


        self.statsLayout.addLayout(self.hpLayout)

        self.acLayout = QHBoxLayout()
        self.acLayout.setObjectName(u"acLayout")
        self.label_2 = QLabel(Monster)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.acLayout.addWidget(self.label_2)

        self.sbAC = QSpinBox(Monster)
        self.sbAC.setObjectName(u"sbAC")
        self.sbAC.setFont(font1)
        self.sbAC.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbAC.setMaximum(9999)

        self.acLayout.addWidget(self.sbAC)


        self.statsLayout.addLayout(self.acLayout)

        self.strLayout = QHBoxLayout()
        self.strLayout.setObjectName(u"strLayout")
        self.label_4 = QLabel(Monster)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.strLayout.addWidget(self.label_4)

        self.sbStr = QSpinBox(Monster)
        self.sbStr.setObjectName(u"sbStr")
        self.sbStr.setFont(font1)
        self.sbStr.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbStr.setMaximum(9999)

        self.strLayout.addWidget(self.sbStr)


        self.statsLayout.addLayout(self.strLayout)

        self.dexLayout = QHBoxLayout()
        self.dexLayout.setObjectName(u"dexLayout")
        self.label_5 = QLabel(Monster)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.dexLayout.addWidget(self.label_5)

        self.sbDex = QSpinBox(Monster)
        self.sbDex.setObjectName(u"sbDex")
        self.sbDex.setFont(font1)
        self.sbDex.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbDex.setMaximum(9999)

        self.dexLayout.addWidget(self.sbDex)


        self.statsLayout.addLayout(self.dexLayout)

        self.conLayout = QHBoxLayout()
        self.conLayout.setObjectName(u"conLayout")
        self.label_6 = QLabel(Monster)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.conLayout.addWidget(self.label_6)

        self.sbCon = QSpinBox(Monster)
        self.sbCon.setObjectName(u"sbCon")
        self.sbCon.setFont(font1)
        self.sbCon.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbCon.setMaximum(9999)

        self.conLayout.addWidget(self.sbCon)


        self.statsLayout.addLayout(self.conLayout)

        self.intLayout = QHBoxLayout()
        self.intLayout.setObjectName(u"intLayout")
        self.label_7 = QLabel(Monster)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.intLayout.addWidget(self.label_7)

        self.sbInt = QSpinBox(Monster)
        self.sbInt.setObjectName(u"sbInt")
        self.sbInt.setFont(font1)
        self.sbInt.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbInt.setMaximum(9999)

        self.intLayout.addWidget(self.sbInt)


        self.statsLayout.addLayout(self.intLayout)

        self.wisLayout = QHBoxLayout()
        self.wisLayout.setObjectName(u"wisLayout")
        self.label_8 = QLabel(Monster)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.wisLayout.addWidget(self.label_8)

        self.sbWis = QSpinBox(Monster)
        self.sbWis.setObjectName(u"sbWis")
        self.sbWis.setFont(font1)
        self.sbWis.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbWis.setMaximum(9999)

        self.wisLayout.addWidget(self.sbWis)


        self.statsLayout.addLayout(self.wisLayout)

        self.chaLayout = QHBoxLayout()
        self.chaLayout.setObjectName(u"chaLayout")
        self.label_9 = QLabel(Monster)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.chaLayout.addWidget(self.label_9)

        self.sbCha = QSpinBox(Monster)
        self.sbCha.setObjectName(u"sbCha")
        self.sbCha.setFont(font1)
        self.sbCha.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbCha.setMaximum(9999)

        self.chaLayout.addWidget(self.sbCha)


        self.statsLayout.addLayout(self.chaLayout)

        self.profLayout = QHBoxLayout()
        self.profLayout.setObjectName(u"profLayout")
        self.label_10 = QLabel(Monster)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.profLayout.addWidget(self.label_10)

        self.sbProf = QSpinBox(Monster)
        self.sbProf.setObjectName(u"sbProf")
        self.sbProf.setFont(font1)
        self.sbProf.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbProf.setMaximum(9999)

        self.profLayout.addWidget(self.sbProf)


        self.statsLayout.addLayout(self.profLayout)

        self.xpLayout = QHBoxLayout()
        self.xpLayout.setObjectName(u"xpLayout")
        self.label_11 = QLabel(Monster)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.xpLayout.addWidget(self.label_11)

        self.sbXP = QSpinBox(Monster)
        self.sbXP.setObjectName(u"sbXP")
        self.sbXP.setFont(font1)
        self.sbXP.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sbXP.setMaximum(9999)

        self.xpLayout.addWidget(self.sbXP)


        self.statsLayout.addLayout(self.xpLayout)


        self.editorLayout.addLayout(self.statsLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editorLayout.addItem(self.horizontalSpacer)

        self.abilitiesLayout = QVBoxLayout()
        self.abilitiesLayout.setObjectName(u"abilitiesLayout")
        self.movementLayout = QVBoxLayout()
        self.movementLayout.setObjectName(u"movementLayout")
        self.label_12 = QLabel(Monster)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.movementLayout.addWidget(self.label_12)

        self.saMovement = QScrollArea(Monster)
        self.saMovement.setObjectName(u"saMovement")
        self.saMovement.setWidgetResizable(True)
        self.saMovementContent = QWidget()
        self.saMovementContent.setObjectName(u"saMovementContent")
        self.saMovementContent.setGeometry(QRect(0, 0, 364, 129))
        self.saMovement.setWidget(self.saMovementContent)

        self.movementLayout.addWidget(self.saMovement)

        self.pbAddMovement = QPushButton(Monster)
        self.pbAddMovement.setObjectName(u"pbAddMovement")

        self.movementLayout.addWidget(self.pbAddMovement)


        self.abilitiesLayout.addLayout(self.movementLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(Monster)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_13)

        self.saActions = QScrollArea(Monster)
        self.saActions.setObjectName(u"saActions")
        self.saActions.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 364, 129))
        self.saActions.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.saActions)

        self.pbAddAction = QPushButton(Monster)
        self.pbAddAction.setObjectName(u"pbAddAction")

        self.verticalLayout_2.addWidget(self.pbAddAction)


        self.abilitiesLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Monster)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.saLegendaryActions = QScrollArea(Monster)
        self.saLegendaryActions.setObjectName(u"saLegendaryActions")
        self.saLegendaryActions.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 364, 129))
        self.saLegendaryActions.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_3.addWidget(self.saLegendaryActions)

        self.pbAddLegendary = QPushButton(Monster)
        self.pbAddLegendary.setObjectName(u"pbAddLegendary")

        self.verticalLayout_3.addWidget(self.pbAddLegendary)


        self.abilitiesLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_14 = QLabel(Monster)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_14)

        self.damageTypesLayout = QHBoxLayout()
        self.damageTypesLayout.setObjectName(u"damageTypesLayout")

        self.verticalLayout_4.addLayout(self.damageTypesLayout)


        self.abilitiesLayout.addLayout(self.verticalLayout_4)


        self.editorLayout.addLayout(self.abilitiesLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.editorLayout.addItem(self.horizontalSpacer_2)

        self.spellsLayout = QVBoxLayout()
        self.spellsLayout.setObjectName(u"spellsLayout")

        self.editorLayout.addLayout(self.spellsLayout)


        self.verticalLayout.addLayout(self.editorLayout)

        self.saveLayout = QVBoxLayout()
        self.saveLayout.setObjectName(u"saveLayout")
        self.pbReset = QPushButton(Monster)
        self.pbReset.setObjectName(u"pbReset")

        self.saveLayout.addWidget(self.pbReset)

        self.pbUpdate = QPushButton(Monster)
        self.pbUpdate.setObjectName(u"pbUpdate")

        self.saveLayout.addWidget(self.pbUpdate)

        self.pbCopy = QPushButton(Monster)
        self.pbCopy.setObjectName(u"pbCopy")

        self.saveLayout.addWidget(self.pbCopy)


        self.verticalLayout.addLayout(self.saveLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Monster)

        QMetaObject.connectSlotsByName(Monster)
    # setupUi

    def retranslateUi(self, Monster):
        Monster.setWindowTitle(QCoreApplication.translate("Monster", u"Form", None))
        self.name.setText(QCoreApplication.translate("Monster", u"Name", None))
        self.cbType.setItemText(0, QCoreApplication.translate("Monster", u"Aberration", None))
        self.cbType.setItemText(1, QCoreApplication.translate("Monster", u"Beast", None))
        self.cbType.setItemText(2, QCoreApplication.translate("Monster", u"Celestial", None))
        self.cbType.setItemText(3, QCoreApplication.translate("Monster", u"Construct", None))
        self.cbType.setItemText(4, QCoreApplication.translate("Monster", u"Dragon", None))
        self.cbType.setItemText(5, QCoreApplication.translate("Monster", u"Elemental", None))
        self.cbType.setItemText(6, QCoreApplication.translate("Monster", u"Fey", None))
        self.cbType.setItemText(7, QCoreApplication.translate("Monster", u"Fiend", None))
        self.cbType.setItemText(8, QCoreApplication.translate("Monster", u"Giant", None))
        self.cbType.setItemText(9, QCoreApplication.translate("Monster", u"Humanoid", None))
        self.cbType.setItemText(10, QCoreApplication.translate("Monster", u"Monstrosity", None))
        self.cbType.setItemText(11, QCoreApplication.translate("Monster", u"Ooze", None))
        self.cbType.setItemText(12, QCoreApplication.translate("Monster", u"Plant", None))
        self.cbType.setItemText(13, QCoreApplication.translate("Monster", u"Undead", None))

        self.cbType.setPlaceholderText(QCoreApplication.translate("Monster", u"Type", None))
        self.pbRace.setText(QCoreApplication.translate("Monster", u"Race(s)", None))
        self.cbSize.setItemText(0, QCoreApplication.translate("Monster", u"Tiny", None))
        self.cbSize.setItemText(1, QCoreApplication.translate("Monster", u"Small", None))
        self.cbSize.setItemText(2, QCoreApplication.translate("Monster", u"Medium", None))
        self.cbSize.setItemText(3, QCoreApplication.translate("Monster", u"Large", None))
        self.cbSize.setItemText(4, QCoreApplication.translate("Monster", u"Huge", None))
        self.cbSize.setItemText(5, QCoreApplication.translate("Monster", u"Gargantuan", None))

        self.cbSize.setPlaceholderText(QCoreApplication.translate("Monster", u"Size", None))
        self.label.setText(QCoreApplication.translate("Monster", u"HP", None))
        self.label_2.setText(QCoreApplication.translate("Monster", u"AC", None))
        self.label_4.setText(QCoreApplication.translate("Monster", u"STR", None))
        self.label_5.setText(QCoreApplication.translate("Monster", u"DEX", None))
        self.label_6.setText(QCoreApplication.translate("Monster", u"CON", None))
        self.label_7.setText(QCoreApplication.translate("Monster", u"INT", None))
        self.label_8.setText(QCoreApplication.translate("Monster", u"WIS", None))
        self.label_9.setText(QCoreApplication.translate("Monster", u"CHA", None))
        self.label_10.setText(QCoreApplication.translate("Monster", u"Prof", None))
        self.label_11.setText(QCoreApplication.translate("Monster", u"XP", None))
        self.label_12.setText(QCoreApplication.translate("Monster", u"Movement", None))
        self.pbAddMovement.setText(QCoreApplication.translate("Monster", u"Add", None))
        self.label_13.setText(QCoreApplication.translate("Monster", u"Actions", None))
        self.pbAddAction.setText(QCoreApplication.translate("Monster", u"Add", None))
        self.label_3.setText(QCoreApplication.translate("Monster", u"Legendary Actions", None))
        self.pbAddLegendary.setText(QCoreApplication.translate("Monster", u"Add", None))
        self.label_14.setText(QCoreApplication.translate("Monster", u"Damage Types", None))
        self.pbReset.setText(QCoreApplication.translate("Monster", u"Reset", None))
        self.pbUpdate.setText(QCoreApplication.translate("Monster", u"Update", None))
        self.pbCopy.setText(QCoreApplication.translate("Monster", u"Copy", None))
    # retranslateUi

