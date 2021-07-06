# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'common_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModernCipherGroupBox(object):
    def setupUi(self, ModernCipherGroupBox):
        if not ModernCipherGroupBox.objectName():
            ModernCipherGroupBox.setObjectName(u"ModernCipherGroupBox")
        ModernCipherGroupBox.resize(667, 468)
        self.verticalLayout = QVBoxLayout(ModernCipherGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textSplitter = QSplitter(ModernCipherGroupBox)
        self.textSplitter.setObjectName(u"textSplitter")
        self.textSplitter.setOrientation(Qt.Horizontal)
        self.textSplitter.setHandleWidth(10)
        self.plainTextGroupBox = QGroupBox(self.textSplitter)
        self.plainTextGroupBox.setObjectName(u"plainTextGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextGroupBox.sizePolicy().hasHeightForWidth())
        self.plainTextGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.plainTextGroupBox)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.plaintextEdit = QPlainTextEdit(self.plainTextGroupBox)
        self.plaintextEdit.setObjectName(u"plaintextEdit")

        self.verticalLayout_2.addWidget(self.plaintextEdit)

        self.plaintextChooseFileButton = QPushButton(self.plainTextGroupBox)
        self.plaintextChooseFileButton.setObjectName(u"plaintextChooseFileButton")

        self.verticalLayout_2.addWidget(self.plaintextChooseFileButton)

        self.textSplitter.addWidget(self.plainTextGroupBox)
        self.cipherTextGroupBox = QGroupBox(self.textSplitter)
        self.cipherTextGroupBox.setObjectName(u"cipherTextGroupBox")
        sizePolicy.setHeightForWidth(self.cipherTextGroupBox.sizePolicy().hasHeightForWidth())
        self.cipherTextGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.cipherTextGroupBox)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.ciphertextEdit = QPlainTextEdit(self.cipherTextGroupBox)
        self.ciphertextEdit.setObjectName(u"ciphertextEdit")

        self.verticalLayout_3.addWidget(self.ciphertextEdit)

        self.ciphertextChooseFileButton = QPushButton(self.cipherTextGroupBox)
        self.ciphertextChooseFileButton.setObjectName(u"ciphertextChooseFileButton")

        self.verticalLayout_3.addWidget(self.ciphertextChooseFileButton)

        self.textSplitter.addWidget(self.cipherTextGroupBox)

        self.verticalLayout.addWidget(self.textSplitter)

        self.keyLayout = QHBoxLayout()
        self.keyLayout.setSpacing(10)
        self.keyLayout.setObjectName(u"keyLayout")
        self.keyLabel = QLabel(ModernCipherGroupBox)
        self.keyLabel.setObjectName(u"keyLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.keyLabel.sizePolicy().hasHeightForWidth())
        self.keyLabel.setSizePolicy(sizePolicy1)
        self.keyLabel.setLayoutDirection(Qt.LeftToRight)

        self.keyLayout.addWidget(self.keyLabel)

        self.keyLineEdit = QLineEdit(ModernCipherGroupBox)
        self.keyLineEdit.setObjectName(u"keyLineEdit")

        self.keyLayout.addWidget(self.keyLineEdit)

        self.keyChooseFile = QPushButton(ModernCipherGroupBox)
        self.keyChooseFile.setObjectName(u"keyChooseFile")

        self.keyLayout.addWidget(self.keyChooseFile)


        self.verticalLayout.addLayout(self.keyLayout)

        self.bottomButtonLayout = QHBoxLayout()
        self.bottomButtonLayout.setObjectName(u"bottomButtonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomButtonLayout.addItem(self.horizontalSpacer)

        self.encryptButton = QPushButton(ModernCipherGroupBox)
        self.encryptButton.setObjectName(u"encryptButton")

        self.bottomButtonLayout.addWidget(self.encryptButton)

        self.decryptButton = QPushButton(ModernCipherGroupBox)
        self.decryptButton.setObjectName(u"decryptButton")

        self.bottomButtonLayout.addWidget(self.decryptButton)

        self.exportButton = QPushButton(ModernCipherGroupBox)
        self.exportButton.setObjectName(u"exportButton")

        self.bottomButtonLayout.addWidget(self.exportButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomButtonLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.bottomButtonLayout)


        self.retranslateUi(ModernCipherGroupBox)

        QMetaObject.connectSlotsByName(ModernCipherGroupBox)
    # setupUi

    def retranslateUi(self, ModernCipherGroupBox):
        ModernCipherGroupBox.setWindowTitle("")
        ModernCipherGroupBox.setTitle(QCoreApplication.translate("ModernCipherGroupBox", u"\u65e0\u6807\u9898", None))
        self.plainTextGroupBox.setTitle(QCoreApplication.translate("ModernCipherGroupBox", u"\u660e\u6587", None))
        self.plaintextChooseFileButton.setText(QCoreApplication.translate("ModernCipherGroupBox", u"\u9009\u62e9\u6587\u4ef6", None))
        self.cipherTextGroupBox.setTitle(QCoreApplication.translate("ModernCipherGroupBox", u"\u5bc6\u6587", None))
        self.ciphertextChooseFileButton.setText(QCoreApplication.translate("ModernCipherGroupBox", u"\u9009\u62e9\u6587\u4ef6", None))
        self.keyLabel.setText(QCoreApplication.translate("ModernCipherGroupBox", u"\u5bc6\u94a5", None))
        self.keyChooseFile.setText(QCoreApplication.translate("ModernCipherGroupBox", u"\u9009\u62e9\u6587\u4ef6", None))
        self.encryptButton.setText(QCoreApplication.translate("ModernCipherGroupBox", u"\u52a0\u5bc6", None))
        self.decryptButton.setText(QCoreApplication.translate("ModernCipherGroupBox", u"\u89e3\u5bc6", None))
        self.exportButton.setText(QCoreApplication.translate("ModernCipherGroupBox", u"\u5bfc\u51fa\u7ed3\u679c", None))
    # retranslateUi

