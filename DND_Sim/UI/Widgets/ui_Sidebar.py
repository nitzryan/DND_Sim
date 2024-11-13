# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Sidebar(object):
    def setupUi(self, Sidebar):
        if not Sidebar.objectName():
            Sidebar.setObjectName(u"Sidebar")
        Sidebar.resize(271, 464)
        self.verticalLayout = QVBoxLayout(Sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_Train = QPushButton(Sidebar)
        self.pb_Train.setObjectName(u"pb_Train")
        self.pb_Train.setSizeIncrement(QSize(1, 1))
        self.pb_Train.setBaseSize(QSize(1, 1))

        self.verticalLayout.addWidget(self.pb_Train)

        self.pb_Editor = QPushButton(Sidebar)
        self.pb_Editor.setObjectName(u"pb_Editor")
        self.pb_Editor.setSizeIncrement(QSize(1, 1))
        self.pb_Editor.setBaseSize(QSize(1, 1))

        self.verticalLayout.addWidget(self.pb_Editor)

        self.pb_Tester = QPushButton(Sidebar)
        self.pb_Tester.setObjectName(u"pb_Tester")
        self.pb_Tester.setSizeIncrement(QSize(1, 1))
        self.pb_Tester.setBaseSize(QSize(1, 1))

        self.verticalLayout.addWidget(self.pb_Tester)

        self.pb_Character = QPushButton(Sidebar)
        self.pb_Character.setObjectName(u"pb_Character")
        self.pb_Character.setSizeIncrement(QSize(1, 1))
        self.pb_Character.setBaseSize(QSize(1, 1))

        self.verticalLayout.addWidget(self.pb_Character)

        self.verticalSpacer = QSpacerItem(20, 353, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Sidebar)

        QMetaObject.connectSlotsByName(Sidebar)
    # setupUi

    def retranslateUi(self, Sidebar):
        Sidebar.setWindowTitle(QCoreApplication.translate("Sidebar", u"Form", None))
        self.pb_Train.setText(QCoreApplication.translate("Sidebar", u"Train", None))
        self.pb_Editor.setText(QCoreApplication.translate("Sidebar", u"Scenario Editor", None))
        self.pb_Tester.setText(QCoreApplication.translate("Sidebar", u"Scenario Tester", None))
        self.pb_Character.setText(QCoreApplication.translate("Sidebar", u"Character Editor", None))
    # retranslateUi

