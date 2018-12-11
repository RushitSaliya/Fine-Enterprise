# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SellingDeleteDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SellingDeleteDataDialog(object):
    def setupUi(self, SellingDeleteDataDialog):
        SellingDeleteDataDialog.setObjectName("SellingDeleteDataDialog")
        SellingDeleteDataDialog.resize(445, 165)
        self.gridLayout = QtWidgets.QGridLayout(SellingDeleteDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_index = QtWidgets.QLabel(SellingDeleteDataDialog)
        self.lbl_index.setObjectName("lbl_index")
        self.gridLayout.addWidget(self.lbl_index, 0, 0, 1, 1)
        self.line_edit_index = QtWidgets.QLineEdit(SellingDeleteDataDialog)
        self.line_edit_index.setObjectName("line_edit_index")
        self.gridLayout.addWidget(self.line_edit_index, 0, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(SellingDeleteDataDialog)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 1, 1, 1, 1)

        self.retranslateUi(SellingDeleteDataDialog)
        QtCore.QMetaObject.connectSlotsByName(SellingDeleteDataDialog)

    def retranslateUi(self, SellingDeleteDataDialog):
        _translate = QtCore.QCoreApplication.translate
        SellingDeleteDataDialog.setWindowTitle(_translate("SellingDeleteDataDialog", "Delete Data"))
        self.lbl_index.setText(_translate("SellingDeleteDataDialog", "Index:"))
        self.btn_delete.setText(_translate("SellingDeleteDataDialog", "Delete"))

