# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'md5.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MD5Widget(object):
    def setupUi(self, MD5Widget):
        if not MD5Widget.objectName():
            MD5Widget.setObjectName(u"MD5Widget")
        MD5Widget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(MD5Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(MD5Widget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.lineEdit = QLineEdit(MD5Widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(MD5Widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(MD5Widget)

        QMetaObject.connectSlotsByName(MD5Widget)
    # setupUi

    def retranslateUi(self, MD5Widget):
        MD5Widget.setWindowTitle(QCoreApplication.translate("MD5Widget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("MD5Widget", u"hash", None))
    # retranslateUi

