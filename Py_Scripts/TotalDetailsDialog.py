# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TotalDetailsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TotalDetailsDialog(object):
    def setupUi(self, TotalDetailsDialog):
        TotalDetailsDialog.setObjectName("TotalDetailsDialog")
        TotalDetailsDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(TotalDetailsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.table_widget_total_details = QtWidgets.QTableWidget(TotalDetailsDialog)
        self.table_widget_total_details.setObjectName("table_widget_total_details")
        self.table_widget_total_details.setColumnCount(0)
        self.table_widget_total_details.setRowCount(0)
        self.gridLayout.addWidget(self.table_widget_total_details, 0, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(TotalDetailsDialog)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 1, 0, 1, 1)

        self.retranslateUi(TotalDetailsDialog)
        QtCore.QMetaObject.connectSlotsByName(TotalDetailsDialog)

    def retranslateUi(self, TotalDetailsDialog):
        _translate = QtCore.QCoreApplication.translate
        TotalDetailsDialog.setWindowTitle(_translate("TotalDetailsDialog", "Totals Details"))
        self.btn_ok.setText(_translate("TotalDetailsDialog", "Ok"))

