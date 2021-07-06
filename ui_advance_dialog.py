# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advance_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AdvanceDialog(object):
    def setupUi(self, AdvanceDialog):
        if not AdvanceDialog.objectName():
            AdvanceDialog.setObjectName(u"AdvanceDialog")
        AdvanceDialog.resize(380, 383)
        self.verticalLayout_2 = QVBoxLayout(AdvanceDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(AdvanceDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.generateKeyTab = QWidget()
        self.generateKeyTab.setObjectName(u"generateKeyTab")
        self.verticalLayout = QVBoxLayout(self.generateKeyTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.publicKeyLineEdit = QLineEdit(self.generateKeyTab)
        self.publicKeyLineEdit.setObjectName(u"publicKeyLineEdit")
        self.publicKeyLineEdit.setReadOnly(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.publicKeyLineEdit)

        self.privateKeyLabel = QLabel(self.generateKeyTab)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.privateKeyLabel)

        self.privateKeyLineEdit = QLineEdit(self.generateKeyTab)
        self.privateKeyLineEdit.setObjectName(u"privateKeyLineEdit")
        self.privateKeyLineEdit.setReadOnly(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.privateKeyLineEdit)

        self.publicKeyLabel = QLabel(self.generateKeyTab)
        self.publicKeyLabel.setObjectName(u"publicKeyLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.publicKeyLabel)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.generateKeyButton = QPushButton(self.generateKeyTab)
        self.generateKeyButton.setObjectName(u"generateKeyButton")

        self.horizontalLayout_2.addWidget(self.generateKeyButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.generateKeyTab, "")
        self.customTab = QWidget()
        self.customTab.setObjectName(u"customTab")
        self.verticalLayout_3 = QVBoxLayout(self.customTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.eLabel = QLabel(self.customTab)
        self.eLabel.setObjectName(u"eLabel")

        self.horizontalLayout.addWidget(self.eLabel)

        self.eLineEdit = QLineEdit(self.customTab)
        self.eLineEdit.setObjectName(u"eLineEdit")

        self.horizontalLayout.addWidget(self.eLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 228, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.customTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(AdvanceDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(AdvanceDialog)
        self.buttonBox.accepted.connect(AdvanceDialog.accept)
        self.buttonBox.rejected.connect(AdvanceDialog.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdvanceDialog)
    # setupUi

    def retranslateUi(self, AdvanceDialog):
        AdvanceDialog.setWindowTitle(QCoreApplication.translate("AdvanceDialog", u"\u9ad8\u7ea7", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("AdvanceDialog", u"\u79c1\u94a5", None))
        self.publicKeyLabel.setText(QCoreApplication.translate("AdvanceDialog", u"\u516c\u94a5", None))
        self.generateKeyButton.setText(QCoreApplication.translate("AdvanceDialog", u"\u751f\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generateKeyTab), QCoreApplication.translate("AdvanceDialog", u"\u751f\u6210\u5bc6\u94a5", None))
        self.eLabel.setText(QCoreApplication.translate("AdvanceDialog", u"e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customTab), QCoreApplication.translate("AdvanceDialog", u"\u81ea\u5b9a\u4e49\u53c2\u6570", None))
    # retranslateUi

