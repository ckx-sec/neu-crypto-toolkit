# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TextEncryptionWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TextEncryptionWidget(object):
    def setupUi(self, TextEncryptionWidget):
        if not TextEncryptionWidget.objectName():
            TextEncryptionWidget.setObjectName(u"TextEncryptionWidget")
        TextEncryptionWidget.resize(524, 427)
        self.verticalLayout = QVBoxLayout(TextEncryptionWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEditsLayout = QHBoxLayout()
        self.textEditsLayout.setObjectName(u"textEditsLayout")
        self.plaintextBox = QGroupBox(TextEncryptionWidget)
        self.plaintextBox.setObjectName(u"plaintextBox")
        self.horizontalLayout_2 = QHBoxLayout(self.plaintextBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.plaintextBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_2.addWidget(self.plainTextEdit)


        self.textEditsLayout.addWidget(self.plaintextBox)

        self.ciphertextBox = QGroupBox(TextEncryptionWidget)
        self.ciphertextBox.setObjectName(u"ciphertextBox")
        self.horizontalLayout_3 = QHBoxLayout(self.ciphertextBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cipherTextEdit = QPlainTextEdit(self.ciphertextBox)
        self.cipherTextEdit.setObjectName(u"cipherTextEdit")

        self.horizontalLayout_3.addWidget(self.cipherTextEdit)


        self.textEditsLayout.addWidget(self.ciphertextBox)


        self.verticalLayout.addLayout(self.textEditsLayout)

        self.keyLayout = QHBoxLayout()
        self.keyLayout.setObjectName(u"keyLayout")
        self.keyLabel = QLabel(TextEncryptionWidget)
        self.keyLabel.setObjectName(u"keyLabel")

        self.keyLayout.addWidget(self.keyLabel)

        self.keyLineEdit = QLineEdit(TextEncryptionWidget)
        self.keyLineEdit.setObjectName(u"keyLineEdit")

        self.keyLayout.addWidget(self.keyLineEdit)


        self.verticalLayout.addLayout(self.keyLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.buttonLayout.addItem(self.buttonSpacer)

        self.encryptPushButton = QPushButton(TextEncryptionWidget)
        self.encryptPushButton.setObjectName(u"encryptPushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.encryptPushButton.sizePolicy().hasHeightForWidth())
        self.encryptPushButton.setSizePolicy(sizePolicy)

        self.buttonLayout.addWidget(self.encryptPushButton)

        self.decryptPushButton = QPushButton(TextEncryptionWidget)
        self.decryptPushButton.setObjectName(u"decryptPushButton")
        sizePolicy.setHeightForWidth(self.decryptPushButton.sizePolicy().hasHeightForWidth())
        self.decryptPushButton.setSizePolicy(sizePolicy)

        self.buttonLayout.addWidget(self.decryptPushButton)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(TextEncryptionWidget)

        QMetaObject.connectSlotsByName(TextEncryptionWidget)
    # setupUi

    def retranslateUi(self, TextEncryptionWidget):
        TextEncryptionWidget.setWindowTitle("")
        self.plaintextBox.setTitle(QCoreApplication.translate("TextEncryptionWidget", u"\u660e\u6587", None))
        self.ciphertextBox.setTitle(QCoreApplication.translate("TextEncryptionWidget", u"\u5bc6\u6587", None))
        self.keyLabel.setText(QCoreApplication.translate("TextEncryptionWidget", u"\u5bc6\u94a5", None))
        self.encryptPushButton.setText(QCoreApplication.translate("TextEncryptionWidget", u"\u52a0\u5bc6", None))
        self.decryptPushButton.setText(QCoreApplication.translate("TextEncryptionWidget", u"\u89e3\u5bc6", None))
    # retranslateUi

