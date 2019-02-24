# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ViewStockDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewStockDialog(object):
    def setupUi(self, ViewStockDialog):
        ViewStockDialog.setObjectName("ViewStockDialog")
        ViewStockDialog.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(ViewStockDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabel_widget_stock = QtWidgets.QTableWidget(ViewStockDialog)
        self.tabel_widget_stock.setObjectName("tabel_widget_stock")
        self.tabel_widget_stock.setColumnCount(0)
        self.tabel_widget_stock.setRowCount(0)
        self.gridLayout.addWidget(self.tabel_widget_stock, 0, 0, 1, 1)
        self.btn_ok = QtWidgets.QPushButton(ViewStockDialog)
        self.btn_ok.setObjectName("btn_ok")
        self.gridLayout.addWidget(self.btn_ok, 1, 0, 1, 1)

        self.retranslateUi(ViewStockDialog)
        QtCore.QMetaObject.connectSlotsByName(ViewStockDialog)

    def retranslateUi(self, ViewStockDialog):
        _translate = QtCore.QCoreApplication.translate
        ViewStockDialog.setWindowTitle(_translate("ViewStockDialog", "Stock"))
        self.btn_ok.setText(_translate("ViewStockDialog", "Ok"))

