# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DeleteDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteDataDialog(object):
    def setupUi(self, DeleteDataDialog):
        DeleteDataDialog.setObjectName("DeleteDataDialog")
        DeleteDataDialog.resize(445, 165)
        self.gridLayout = QtWidgets.QGridLayout(DeleteDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_index = QtWidgets.QLabel(DeleteDataDialog)
        self.lbl_index.setObjectName("lbl_index")
        self.gridLayout.addWidget(self.lbl_index, 0, 0, 1, 1)
        self.line_edit_index = QtWidgets.QLineEdit(DeleteDataDialog)
        self.line_edit_index.setObjectName("line_edit_index")
        self.gridLayout.addWidget(self.line_edit_index, 0, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(DeleteDataDialog)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 1, 1, 1, 1)

        self.retranslateUi(DeleteDataDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteDataDialog)

    def retranslateUi(self, DeleteDataDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteDataDialog.setWindowTitle(_translate("DeleteDataDialog", "Delete Data"))
        self.lbl_index.setText(_translate("DeleteDataDialog", "Index:"))
        self.btn_delete.setText(_translate("DeleteDataDialog", "Delete"))

