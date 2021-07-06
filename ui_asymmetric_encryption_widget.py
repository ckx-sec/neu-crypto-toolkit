# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asymmetric_encryption_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AsymmetricEncryptionWidget(object):
    def setupUi(self, AsymmetricEncryptionWidget):
        if not AsymmetricEncryptionWidget.objectName():
            AsymmetricEncryptionWidget.setObjectName(u"AsymmetricEncryptionWidget")
        AsymmetricEncryptionWidget.resize(659, 526)
        self.verticalLayout = QVBoxLayout(AsymmetricEncryptionWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textsLayout = QHBoxLayout()
        self.textsLayout.setObjectName(u"textsLayout")
        self.plainLayout = QVBoxLayout()
        self.plainLayout.setObjectName(u"plainLayout")
        self.plainTabWidget = QTabWidget(AsymmetricEncryptionWidget)
        self.plainTabWidget.setObjectName(u"plainTabWidget")
        self.plainTextTab = QWidget()
        self.plainTextTab.setObjectName(u"plainTextTab")
        self.horizontalLayout = QHBoxLayout(self.plainTextTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QTextEdit(self.plainTextTab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.plainTabWidget.addTab(self.plainTextTab, "")
        self.plainFileTab = QWidget()
        self.plainFileTab.setObjectName(u"plainFileTab")
        self.verticalLayout_4 = QVBoxLayout(self.plainFileTab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.plainFileLabel = QLabel(self.plainFileTab)
        self.plainFileLabel.setObjectName(u"plainFileLabel")
        self.plainFileLabel.setAlignment(Qt.AlignCenter)
        self.plainFileLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.plainFileLabel)

        self.plainChooseFileButton = QPushButton(self.plainFileTab)
        self.plainChooseFileButton.setObjectName(u"plainChooseFileButton")

        self.verticalLayout_4.addWidget(self.plainChooseFileButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.plainTabWidget.addTab(self.plainFileTab, "")

        self.plainLayout.addWidget(self.plainTabWidget)


        self.textsLayout.addLayout(self.plainLayout)

        self.cipherLayout = QVBoxLayout()
        self.cipherLayout.setObjectName(u"cipherLayout")
        self.cipherTabWidget = QTabWidget(AsymmetricEncryptionWidget)
        self.cipherTabWidget.setObjectName(u"cipherTabWidget")
        self.cipherTextTab = QWidget()
        self.cipherTextTab.setObjectName(u"cipherTextTab")
        self.horizontalLayout_2 = QHBoxLayout(self.cipherTextTab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cipherTextEdit = QTextEdit(self.cipherTextTab)
        self.cipherTextEdit.setObjectName(u"cipherTextEdit")

        self.horizontalLayout_2.addWidget(self.cipherTextEdit)

        self.cipherTabWidget.addTab(self.cipherTextTab, "")
        self.cipherFileTab = QWidget()
        self.cipherFileTab.setObjectName(u"cipherFileTab")
        self.verticalLayout_5 = QVBoxLayout(self.cipherFileTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.cipherFileLabel = QLabel(self.cipherFileTab)
        self.cipherFileLabel.setObjectName(u"cipherFileLabel")
        self.cipherFileLabel.setAlignment(Qt.AlignCenter)
        self.cipherFileLabel.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.cipherFileLabel)

        self.cipherChooseFileButton = QPushButton(self.cipherFileTab)
        self.cipherChooseFileButton.setObjectName(u"cipherChooseFileButton")

        self.verticalLayout_5.addWidget(self.cipherChooseFileButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.cipherTabWidget.addTab(self.cipherFileTab, "")

        self.cipherLayout.addWidget(self.cipherTabWidget)


        self.textsLayout.addLayout(self.cipherLayout)

        self.textsLayout.setStretch(0, 1)
        self.textsLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.textsLayout)

        self.keyWidget = QWidget(AsymmetricEncryptionWidget)
        self.keyWidget.setObjectName(u"keyWidget")
        self.keyLayout = QHBoxLayout(self.keyWidget)
        self.keyLayout.setObjectName(u"keyLayout")
        self.keyLayout.setContentsMargins(0, 0, 0, 0)
        self.keyLabel = QLabel(self.keyWidget)
        self.keyLabel.setObjectName(u"keyLabel")

        self.keyLayout.addWidget(self.keyLabel)

        self.keyLineEdit = QLineEdit(self.keyWidget)
        self.keyLineEdit.setObjectName(u"keyLineEdit")

        self.keyLayout.addWidget(self.keyLineEdit)

        self.keyImportButton = QPushButton(self.keyWidget)
        self.keyImportButton.setObjectName(u"keyImportButton")

        self.keyLayout.addWidget(self.keyImportButton)


        self.verticalLayout.addWidget(self.keyWidget)

        self.publicKeyWidget = QWidget(AsymmetricEncryptionWidget)
        self.publicKeyWidget.setObjectName(u"publicKeyWidget")
        self.publicKeyLayout = QHBoxLayout(self.publicKeyWidget)
        self.publicKeyLayout.setObjectName(u"publicKeyLayout")
        self.publicKeyLayout.setContentsMargins(0, 0, 0, 0)
        self.publicKeyLabel = QLabel(self.publicKeyWidget)
        self.publicKeyLabel.setObjectName(u"publicKeyLabel")

        self.publicKeyLayout.addWidget(self.publicKeyLabel)

        self.publicKeyLineEdit = QLineEdit(self.publicKeyWidget)
        self.publicKeyLineEdit.setObjectName(u"publicKeyLineEdit")

        self.publicKeyLayout.addWidget(self.publicKeyLineEdit)

        self.importPublicKeyButton = QPushButton(self.publicKeyWidget)
        self.importPublicKeyButton.setObjectName(u"importPublicKeyButton")

        self.publicKeyLayout.addWidget(self.importPublicKeyButton)


        self.verticalLayout.addWidget(self.publicKeyWidget)

        self.privateKeyWidget = QWidget(AsymmetricEncryptionWidget)
        self.privateKeyWidget.setObjectName(u"privateKeyWidget")
        self.privateKeyLayout = QHBoxLayout(self.privateKeyWidget)
        self.privateKeyLayout.setObjectName(u"privateKeyLayout")
        self.privateKeyLayout.setContentsMargins(0, 0, 0, 0)
        self.privateKeyLabel = QLabel(self.privateKeyWidget)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")

        self.privateKeyLayout.addWidget(self.privateKeyLabel)

        self.privateKeyLineEdit = QLineEdit(self.privateKeyWidget)
        self.privateKeyLineEdit.setObjectName(u"privateKeyLineEdit")

        self.privateKeyLayout.addWidget(self.privateKeyLineEdit)

        self.importPrivateKeyButton = QPushButton(self.privateKeyWidget)
        self.importPrivateKeyButton.setObjectName(u"importPrivateKeyButton")

        self.privateKeyLayout.addWidget(self.importPrivateKeyButton)


        self.verticalLayout.addWidget(self.privateKeyWidget)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.advancesButton = QPushButton(AsymmetricEncryptionWidget)
        self.advancesButton.setObjectName(u"advancesButton")

        self.bottomLayout.addWidget(self.advancesButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomLayout.addItem(self.horizontalSpacer)

        self.encryptButton = QPushButton(AsymmetricEncryptionWidget)
        self.encryptButton.setObjectName(u"encryptButton")

        self.bottomLayout.addWidget(self.encryptButton)

        self.decryptButton = QPushButton(AsymmetricEncryptionWidget)
        self.decryptButton.setObjectName(u"decryptButton")

        self.bottomLayout.addWidget(self.decryptButton)


        self.verticalLayout.addLayout(self.bottomLayout)


        self.retranslateUi(AsymmetricEncryptionWidget)

        self.plainTabWidget.setCurrentIndex(0)
        self.cipherTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AsymmetricEncryptionWidget)
    # setupUi

    def retranslateUi(self, AsymmetricEncryptionWidget):
        AsymmetricEncryptionWidget.setWindowTitle(QCoreApplication.translate("AsymmetricEncryptionWidget", u"Form", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u660e\u6587", None))
        self.plainTabWidget.setTabText(self.plainTabWidget.indexOf(self.plainTextTab), QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u6587\u672c", None))
        self.plainFileLabel.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5df2\u9009\u6587\u4ef6\uff1aasdf.zxcv", None))
        self.plainChooseFileButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u9009\u62e9\u660e\u6587\u6587\u4ef6", None))
        self.plainTabWidget.setTabText(self.plainTabWidget.indexOf(self.plainFileTab), QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u6587\u4ef6", None))
        self.cipherTextEdit.setPlaceholderText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u5bc6\u6587", None))
        self.cipherTabWidget.setTabText(self.cipherTabWidget.indexOf(self.cipherTextTab), QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u6587\u672c", None))
        self.cipherFileLabel.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5df2\u9009\u6587\u4ef6\uff1azxcv.asdf", None))
        self.cipherChooseFileButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u9009\u62e9\u5bc6\u6587\u6587\u4ef6", None))
        self.cipherTabWidget.setTabText(self.cipherTabWidget.indexOf(self.cipherFileTab), QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u6587\u4ef6", None))
        self.keyLabel.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5bc6\u94a5", None))
        self.keyLineEdit.setPlaceholderText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u6216\u5bfc\u5165\u6587\u4ef6", None))
        self.keyImportButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5bfc\u5165...", None))
        self.publicKeyLabel.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u516c\u94a5", None))
        self.publicKeyLineEdit.setPlaceholderText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u6216\u5bfc\u5165\u6587\u4ef6", None))
        self.importPublicKeyButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5bfc\u5165...", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u79c1\u94a5", None))
        self.privateKeyLineEdit.setPlaceholderText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u6216\u5bfc\u5165\u6587\u4ef6", None))
        self.importPrivateKeyButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u5bfc\u5165...", None))
        self.advancesButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u9ad8\u7ea7...", None))
        self.encryptButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u52a0\u5bc6", None))
        self.decryptButton.setText(QCoreApplication.translate("AsymmetricEncryptionWidget", u"\u89e3\u5bc6", None))
    # retranslateUi

