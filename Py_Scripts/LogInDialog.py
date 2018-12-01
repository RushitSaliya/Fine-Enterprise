# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogInDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(273, 182)
        self.gridLayout = QtWidgets.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_login = QtWidgets.QPushButton(LoginDialog)
        self.btn_login.setObjectName("btn_login")
        self.gridLayout.addWidget(self.btn_login, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.line_edit_password = QtWidgets.QLineEdit(LoginDialog)
        self.line_edit_password.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.line_edit_password.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setObjectName("line_edit_password")
        self.gridLayout.addWidget(self.line_edit_password, 5, 0, 1, 1)
        self.lbl_login = QtWidgets.QLabel(LoginDialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_login.setFont(font)
        self.lbl_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_login.setObjectName("lbl_login")
        self.gridLayout.addWidget(self.lbl_login, 1, 0, 1, 1)

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Log In"))
        self.btn_login.setText(_translate("LoginDialog", "Log In"))
        self.label_2.setText(_translate("LoginDialog", "Password:"))
        self.lbl_login.setText(_translate("LoginDialog", "Log In"))

