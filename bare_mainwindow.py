# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bare_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainSplitter = QSplitter(self.centralwidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Horizontal)
        self.mainSplitter.setHandleWidth(6)
        self.widget = QWidget(self.mainSplitter)
        self.widget.setObjectName(u"widget")
        self.listAndSearchLayout = QVBoxLayout(self.widget)
        self.listAndSearchLayout.setObjectName(u"listAndSearchLayout")
        self.listAndSearchLayout.setContentsMargins(0, 0, 0, 0)
        self.searchBoxLineEdit = QLineEdit(self.widget)
        self.searchBoxLineEdit.setObjectName(u"searchBoxLineEdit")

        self.listAndSearchLayout.addWidget(self.searchBoxLineEdit)

        self.cipherListWidget = QListWidget(self.widget)
        self.cipherListWidget.setObjectName(u"cipherListWidget")

        self.listAndSearchLayout.addWidget(self.cipherListWidget)

        self.mainSplitter.addWidget(self.widget)
        self.dummyLabel = QLabel(self.mainSplitter)
        self.dummyLabel.setObjectName(u"dummyLabel")
        self.dummyLabel.setFrameShape(QFrame.StyledPanel)
        self.dummyLabel.setFrameShadow(QFrame.Raised)
        self.dummyLabel.setAlignment(Qt.AlignCenter)
        self.mainSplitter.addWidget(self.dummyLabel)

        self.horizontalLayout.addWidget(self.mainSplitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 35))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.searchBoxLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22...", None))
        self.dummyLabel.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e00\u4e2a\u7b97\u6cd5", None))
    # retranslateUi

