# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MonsterMovement.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_MonsterMovement(object):
    def setupUi(self, MonsterMovement):
        if not MonsterMovement.objectName():
            MonsterMovement.setObjectName(u"MonsterMovement")
        MonsterMovement.resize(400, 117)
        self.horizontalLayout = QHBoxLayout(MonsterMovement)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(MonsterMovement)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.spinBox = QSpinBox(MonsterMovement)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QSize(50, 0))
        font = QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(999)

        self.horizontalLayout.addWidget(self.spinBox)

        self.horizontalSpacer = QSpacerItem(209, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(MonsterMovement)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(MonsterMovement)

        QMetaObject.connectSlotsByName(MonsterMovement)
    # setupUi

    def retranslateUi(self, MonsterMovement):
        MonsterMovement.setWindowTitle(QCoreApplication.translate("MonsterMovement", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("MonsterMovement", u"X", None))
    # retranslateUi

