# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DamageButton.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DamageButton(object):
    def setupUi(self, DamageButton):
        if not DamageButton.objectName():
            DamageButton.setObjectName(u"DamageButton")
        DamageButton.resize(400, 300)
        DamageButton.setStyleSheet(u"QPushButton {\n"
"	border: 0.1em solid black;\n"
"	border-radius: 1em;\n"
"	max-width: 2em;\n"
"	max-height: 2em;\n"
"	min-width: 2em;\n"
"	min-height: 2em;\n"
"}\n"
"\n"
"QToolTip {\n"
"	color: black;\n"
"	background-color: white;\n"
"	border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(DamageButton)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DamageButton)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(DamageButton)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.retranslateUi(DamageButton)

        QMetaObject.connectSlotsByName(DamageButton)
    # setupUi

    def retranslateUi(self, DamageButton):
        DamageButton.setWindowTitle(QCoreApplication.translate("DamageButton", u"Form", None))
        self.label.setText(QCoreApplication.translate("DamageButton", u"TextLabel", None))
        self.pushButton.setText("")
    # retranslateUi

