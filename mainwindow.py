# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(275, 377)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(275, 377))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.BASE_URL = QtWidgets.QLabel(self.centralwidget)
        self.BASE_URL.setObjectName("BASE_URL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.BASE_URL)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.API_KEY = QtWidgets.QLabel(self.centralwidget)
        self.API_KEY.setObjectName("API_KEY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.API_KEY)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.API_SECRET = QtWidgets.QLabel(self.centralwidget)
        self.API_SECRET.setObjectName("API_SECRET")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.API_SECRET)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.SYMBOL = QtWidgets.QLabel(self.centralwidget)
        self.SYMBOL.setObjectName("SYMBOL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.SYMBOL)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.N = QtWidgets.QLabel(self.centralwidget)
        self.N.setObjectName("N")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.N)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.verticalLayout.addLayout(self.formLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bmbot"))
        self.BASE_URL.setText(_translate("MainWindow", "BASE_URL"))
        self.lineEdit.setText(_translate("MainWindow", "https://testnet.bitmex.com/api/v1/"))
        self.API_KEY.setText(_translate("MainWindow", "API_KEY"))
        self.lineEdit_2.setText(_translate("MainWindow", "RqRYuYsw-OARqYGok7yympAk"))
        self.API_SECRET.setText(_translate("MainWindow", "API_SECRET"))
        self.lineEdit_3.setText(_translate("MainWindow", "zzrPKzzyzx4XA6joo4DKeLRGyhunz9Pf8IKpsXlqjjLal43G"))
        self.SYMBOL.setText(_translate("MainWindow", "SYMBOL"))
        self.lineEdit_4.setText(_translate("MainWindow", "XBTUSD"))
        self.N.setText(_translate("MainWindow", "N"))
        self.lineEdit_5.setText(_translate("MainWindow", "10"))
        self.pushButton.setText(_translate("MainWindow", "Start"))

import res

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
