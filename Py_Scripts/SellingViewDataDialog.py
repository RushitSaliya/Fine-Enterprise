# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SellingViewDataDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SellingViewData(object):
    def setupUi(self, SellingViewData):
        SellingViewData.setObjectName("SellingViewData")
        SellingViewData.resize(428, 330)
        self.gridLayout = QtWidgets.QGridLayout(SellingViewData)
        self.gridLayout.setObjectName("gridLayout")
        self.table_widget_view_data = QtWidgets.QTableWidget(SellingViewData)
        self.table_widget_view_data.setObjectName("table_widget_view_data")
        self.table_widget_view_data.setColumnCount(0)
        self.table_widget_view_data.setRowCount(0)
        self.gridLayout.addWidget(self.table_widget_view_data, 0, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(SellingViewData)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 1, 0, 1, 1)

        self.retranslateUi(SellingViewData)
        QtCore.QMetaObject.connectSlotsByName(SellingViewData)

    def retranslateUi(self, SellingViewData):
        _translate = QtCore.QCoreApplication.translate
        SellingViewData.setWindowTitle(_translate("SellingViewData", "View Data"))
        self.btn_ok.setText(_translate("SellingViewData", "Ok"))

