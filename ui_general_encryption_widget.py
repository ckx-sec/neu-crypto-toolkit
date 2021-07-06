# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'general_encryption_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GeneralEncryptionWidget(object):
    def setupUi(self, GeneralEncryptionWidget):
        if not GeneralEncryptionWidget.objectName():
            GeneralEncryptionWidget.setObjectName(u"GeneralEncryptionWidget")
        GeneralEncryptionWidget.resize(625, 524)
        self.verticalLayout_3 = QVBoxLayout(GeneralEncryptionWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textsLayout = QHBoxLayout()
        self.textsLayout.setObjectName(u"textsLayout")
        self.plainLayout = QVBoxLayout()
        self.plainLayout.setObjectName(u"plainLayout")
        self.plainTabWidget = QTabWidget(GeneralEncryptionWidget)
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
        self.cipherTabWidget = QTabWidget(GeneralEncryptionWidget)
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

        self.verticalLayout_3.addLayout(self.textsLayout)

        self.keyLayout = QHBoxLayout()
        self.keyLayout.setObjectName(u"keyLayout")
        self.keyLabel = QLabel(GeneralEncryptionWidget)
        self.keyLabel.setObjectName(u"keyLabel")

        self.keyLayout.addWidget(self.keyLabel)

        self.keyLineEdit = QLineEdit(GeneralEncryptionWidget)
        self.keyLineEdit.setObjectName(u"keyLineEdit")

        self.keyLayout.addWidget(self.keyLineEdit)

        self.keyImportButton = QPushButton(GeneralEncryptionWidget)
        self.keyImportButton.setObjectName(u"keyImportButton")

        self.keyLayout.addWidget(self.keyImportButton)


        self.verticalLayout_3.addLayout(self.keyLayout)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomLayout.addItem(self.horizontalSpacer)

        self.encryptButton = QPushButton(GeneralEncryptionWidget)
        self.encryptButton.setObjectName(u"encryptButton")

        self.bottomLayout.addWidget(self.encryptButton)

        self.decryptButton = QPushButton(GeneralEncryptionWidget)
        self.decryptButton.setObjectName(u"decryptButton")

        self.bottomLayout.addWidget(self.decryptButton)


        self.verticalLayout_3.addLayout(self.bottomLayout)


        self.retranslateUi(GeneralEncryptionWidget)

        self.plainTabWidget.setCurrentIndex(0)
        self.cipherTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GeneralEncryptionWidget)
    # setupUi

    def retranslateUi(self, GeneralEncryptionWidget):
        GeneralEncryptionWidget.setWindowTitle(QCoreApplication.translate("GeneralEncryptionWidget", u"Form", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u660e\u6587", None))
        self.plainTabWidget.setTabText(self.plainTabWidget.indexOf(self.plainTextTab), QCoreApplication.translate("GeneralEncryptionWidget", u"\u6587\u672c", None))
        self.plainFileLabel.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u5df2\u9009\u6587\u4ef6\uff1aasdf.zxcv", None))
        self.plainChooseFileButton.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u9009\u62e9\u660e\u6587\u6587\u4ef6", None))
        self.plainTabWidget.setTabText(self.plainTabWidget.indexOf(self.plainFileTab), QCoreApplication.translate("GeneralEncryptionWidget", u"\u6587\u4ef6", None))
        self.cipherTextEdit.setPlaceholderText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u5bc6\u6587", None))
        self.cipherTabWidget.setTabText(self.cipherTabWidget.indexOf(self.cipherTextTab), QCoreApplication.translate("GeneralEncryptionWidget", u"\u6587\u672c", None))
        self.cipherFileLabel.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u5df2\u9009\u6587\u4ef6\uff1azxcv.asdf", None))
        self.cipherChooseFileButton.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u9009\u62e9\u5bc6\u6587\u6587\u4ef6", None))
        self.cipherTabWidget.setTabText(self.cipherTabWidget.indexOf(self.cipherFileTab), QCoreApplication.translate("GeneralEncryptionWidget", u"\u6587\u4ef6", None))
        self.keyLabel.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u5bc6\u94a5", None))
        self.keyLineEdit.setPlaceholderText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u5728\u6b64\u8f93\u5165\u5bc6\u94a5\u6216\u5bfc\u5165\u5bc6\u94a5\u6587\u4ef6", None))
        self.keyImportButton.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u5bfc\u5165\u5bc6\u94a5", None))
        self.encryptButton.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u52a0\u5bc6", None))
        self.decryptButton.setText(QCoreApplication.translate("GeneralEncryptionWidget", u"\u89e3\u5bc6", None))
    # retranslateUi

