# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginForm(object):
    def setupUi(self, loginForm):
        loginForm.setObjectName("loginForm")
        loginForm.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginForm.sizePolicy().hasHeightForWidth())
        loginForm.setSizePolicy(sizePolicy)
        loginForm.setAutoFillBackground(False)
        self.Account = QtWidgets.QLineEdit(loginForm)
        self.Account.setGeometry(QtCore.QRect(210, 100, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Account.setFont(font)
        self.Account.setText("")
        self.Account.setObjectName("Account")
        self.Password = QtWidgets.QLineEdit(loginForm)
        self.Password.setGeometry(QtCore.QRect(210, 220, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.Login = QtWidgets.QPushButton(loginForm)
        self.Login.setGeometry(QtCore.QRect(210, 340, 111, 41))
        self.Login.setObjectName("Login")
        self.Registe = QtWidgets.QPushButton(loginForm)
        self.Registe.setGeometry(QtCore.QRect(410, 340, 111, 41))
        self.Registe.setObjectName("Registe")

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

    def retranslateUi(self, loginForm):
        _translate = QtCore.QCoreApplication.translate
        loginForm.setWindowTitle(_translate("loginForm", "登录"))
        self.Account.setPlaceholderText(_translate("loginForm", "输入用户名"))
        self.Password.setPlaceholderText(_translate("loginForm", "输入密码"))
        self.Login.setText(_translate("loginForm", "登录"))
        self.Registe.setText(_translate("loginForm", "注册"))