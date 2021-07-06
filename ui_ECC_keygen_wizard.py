# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ECC_keygen_wizard.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ECCKeygenWizard(object):
    def setupUi(self, ECCKeygenWizard):
        if not ECCKeygenWizard.objectName():
            ECCKeygenWizard.setObjectName(u"ECCKeygenWizard")
        ECCKeygenWizard.resize(640, 480)
        self.wizardPage0 = QWizardPage()
        self.wizardPage0.setObjectName(u"wizardPage0")
        self.verticalLayout = QVBoxLayout(self.wizardPage0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(self.wizardPage0)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.wizardPage0)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.aLineEdit = QLineEdit(self.wizardPage0)
        self.aLineEdit.setObjectName(u"aLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.aLineEdit)

        self.label_3 = QLabel(self.wizardPage0)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.bLineEdit = QLineEdit(self.wizardPage0)
        self.bLineEdit.setObjectName(u"bLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.bLineEdit)

        self.label_4 = QLabel(self.wizardPage0)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.pLineEdit = QLineEdit(self.wizardPage0)
        self.pLineEdit.setObjectName(u"pLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        ECCKeygenWizard.setPage(0, self.wizardPage0)
        self.wizardPage1 = QWizardPage()
        self.wizardPage1.setObjectName(u"wizardPage1")
        self.verticalLayout_2 = QVBoxLayout(self.wizardPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.wizardPage1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.axisLabel = QLabel(self.wizardPage1)
        self.axisLabel.setObjectName(u"axisLabel")
        font = QFont()
        font.setFamily(u"Noto Sans Mono CJK SC")
        self.axisLabel.setFont(font)
        self.axisLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.axisLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.wizardPage1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.gxLineEdit = QLineEdit(self.wizardPage1)
        self.gxLineEdit.setObjectName(u"gxLineEdit")

        self.horizontalLayout.addWidget(self.gxLineEdit)

        self.label_8 = QLabel(self.wizardPage1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.gyLineEdit = QLineEdit(self.wizardPage1)
        self.gyLineEdit.setObjectName(u"gyLineEdit")

        self.horizontalLayout.addWidget(self.gyLineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(1, 1)
        ECCKeygenWizard.setPage(1, self.wizardPage1)
        self.wizardPage2 = QWizardPage()
        self.wizardPage2.setObjectName(u"wizardPage2")
        self.verticalLayout_3 = QVBoxLayout(self.wizardPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.privateKeyHintLabel = QLabel(self.wizardPage2)
        self.privateKeyHintLabel.setObjectName(u"privateKeyHintLabel")

        self.verticalLayout_3.addWidget(self.privateKeyHintLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.wizardPage2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.inputPrivateKeyLineEdit = QLineEdit(self.wizardPage2)
        self.inputPrivateKeyLineEdit.setObjectName(u"inputPrivateKeyLineEdit")

        self.horizontalLayout_2.addWidget(self.inputPrivateKeyLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        ECCKeygenWizard.setPage(2, self.wizardPage2)
        self.wizardPage3 = QWizardPage()
        self.wizardPage3.setObjectName(u"wizardPage3")
        self.verticalLayout_4 = QVBoxLayout(self.wizardPage3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_15 = QLabel(self.wizardPage3)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.publicKeyLineEdit = QLineEdit(self.wizardPage3)
        self.publicKeyLineEdit.setObjectName(u"publicKeyLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.publicKeyLineEdit)

        self.label_16 = QLabel(self.wizardPage3)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.privateKeyLineEdit = QLineEdit(self.wizardPage3)
        self.privateKeyLineEdit.setObjectName(u"privateKeyLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.privateKeyLineEdit)


        self.verticalLayout_4.addLayout(self.formLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        ECCKeygenWizard.setPage(3, self.wizardPage3)

        self.retranslateUi(ECCKeygenWizard)

        QMetaObject.connectSlotsByName(ECCKeygenWizard)
    # setupUi

    def retranslateUi(self, ECCKeygenWizard):
        ECCKeygenWizard.setWindowTitle(QCoreApplication.translate("ECCKeygenWizard", u"ECC\u5bc6\u94a5\u751f\u6210\u5411\u5bfc", None))
        self.wizardPage0.setTitle(QCoreApplication.translate("ECCKeygenWizard", u"\u751f\u6210\u692d\u5706\u66f2\u7ebf", None))
        self.label_11.setText(QCoreApplication.translate("ECCKeygenWizard", u"\u8bf7\u6307\u5b9a\u692d\u5706\u66f2\u7ebf\u7684\u53c2\u6570a\u3001b\u3001p\uff08p\u4e3a\u8d28\u6570\uff09", None))
        self.label_2.setText(QCoreApplication.translate("ECCKeygenWizard", u"a", None))
        self.aLineEdit.setPlaceholderText(QCoreApplication.translate("ECCKeygenWizard", u"\u6574\u6570", None))
        self.label_3.setText(QCoreApplication.translate("ECCKeygenWizard", u"b", None))
        self.bLineEdit.setPlaceholderText(QCoreApplication.translate("ECCKeygenWizard", u"\u6574\u6570", None))
        self.label_4.setText(QCoreApplication.translate("ECCKeygenWizard", u"p", None))
        self.pLineEdit.setPlaceholderText(QCoreApplication.translate("ECCKeygenWizard", u"\u8d28\u6570", None))
        self.wizardPage1.setTitle(QCoreApplication.translate("ECCKeygenWizard", u"\u9009\u62e9\u57fa\u70b9\u5750\u6807", None))
        self.wizardPage1.setSubTitle("")
        self.label_5.setText(QCoreApplication.translate("ECCKeygenWizard", u"\u8bf7\u5728\u5982\u4e0b\u5750\u6807\u7cfb\u4e2d\u9009\u4e00\u4e2a\u70b9\u4f5c\u4e3a\u57fa\u70b9G\u7684\u5750\u6807", None))
        self.axisLabel.setText(QCoreApplication.translate("ECCKeygenWizard", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("ECCKeygenWizard", u"<html><head/><body><p>G<span style=\" vertical-align:sub;\">x</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("ECCKeygenWizard", u"<html><head/><body><p>G<span style=\" vertical-align:sub;\">y</span></p></body></html>", None))
        self.wizardPage2.setTitle(QCoreApplication.translate("ECCKeygenWizard", u"\u9009\u62e9\u79c1\u94a5\uff08k\uff09", None))
        self.privateKeyHintLabel.setText(QCoreApplication.translate("ECCKeygenWizard", u"\u8bf7\u8f93\u5165\u4e00\u4e2a\u5c0f\u4e8e?\u7684\u6b63\u6574\u6570", None))
        self.label_10.setText(QCoreApplication.translate("ECCKeygenWizard", u"\u79c1\u94a5", None))
        self.wizardPage3.setTitle(QCoreApplication.translate("ECCKeygenWizard", u"\u5b8c\u6210", None))
        self.label_15.setText(QCoreApplication.translate("ECCKeygenWizard", u"\u516c\u94a5", None))
        self.label_16.setText(QCoreApplication.translate("ECCKeygenWizard", u"\u79c1\u94a5", None))
    # retranslateUi

