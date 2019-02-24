# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SellingViewDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SellingViewDataDialog(object):
    def setupUi(self, SellingViewDataDialog):
        SellingViewDataDialog.setObjectName("SellingViewDataDialog")
        SellingViewDataDialog.resize(428, 330)
        self.gridLayout = QtWidgets.QGridLayout(SellingViewDataDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.table_widget_view_data = QtWidgets.QTableWidget(SellingViewDataDialog)
        self.table_widget_view_data.setObjectName("table_widget_view_data")
        self.table_widget_view_data.setColumnCount(0)
        self.table_widget_view_data.setRowCount(0)
        self.gridLayout.addWidget(self.table_widget_view_data, 0, 1, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(SellingViewDataDialog)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 2, 1, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(SellingViewDataDialog)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout.addWidget(self.btn_delete, 1, 1, 1, 1)

        self.retranslateUi(SellingViewDataDialog)
        QtCore.QMetaObject.connectSlotsByName(SellingViewDataDialog)

    def retranslateUi(self, SellingViewDataDialog):
        _translate = QtCore.QCoreApplication.translate
        SellingViewDataDialog.setWindowTitle(_translate("SellingViewDataDialog", "View Data"))
        self.btn_ok.setText(_translate("SellingViewDataDialog", "Ok"))
        self.btn_delete.setText(_translate("SellingViewDataDialog", "Delete"))

