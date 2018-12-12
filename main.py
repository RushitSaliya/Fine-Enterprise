"""
Data Entry desktop app for Fine Enterprise
"""

import sys
import pandas as pd
import csv
import warnings
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from Py_Scripts import LogInDialog, MainDialog, ViewStockDialog, DeleteDataDialog, SellingEnterDataDialog, \
    SellingViewDataDialog, TotalDetailsDialog, PurchaseEnterDataDialog


class MainDialogWindow(QDialog, MainDialog.Ui_MainDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.view_stock_window_obj = None

        self.selling_enter_data_window_obj = None
        self.purchase_enter_data_window_obj = None

        self.selling_view_and_delete_data_window_obj = None
        self.purchase_view_and_delete_data_window_obj = None

        self.total_details_window_obj = None

        self.btn_enter_data.hide()
        self.btn_view_and_delete_data.hide()

        self.btn_stock.clicked.connect(self.pop_up_stock_dialog)

        self.btn_enter_data.clicked.connect(self.pop_up_enter_data_dialog)
        self.btn_view_and_delete_data.clicked.connect(self.pop_up_view_data_dialog)
        self.btn_toal_details.clicked.connect(self.pop_up_total_details)

    def pop_up_stock_dialog(self):
        self.view_stock_window_obj = ViewStockDialogWindow()
        self.view_stock_window_obj.retranslateUi(self.view_stock_window_obj)
        self.view_stock_window_obj.show()

    def pop_up_view_data_dialog(self):
        if self.radio_btn_selling.isChecked():
            self.selling_view_and_delete_data_window_obj = SellingViewDataDialogWindow()
            self.selling_view_and_delete_data_window_obj.retranslateUi(self.selling_view_and_delete_data_window_obj)
            self.selling_view_and_delete_data_window_obj.show()
        else:
            self.purchase_view_and_delete_data_window_obj = PurchaseViewDataDialogWindow()
            self.purchase_view_and_delete_data_window_obj.retranslateUi(self.purchase_view_and_delete_data_window_obj)
            self.purchase_view_and_delete_data_window_obj.show()

    def pop_up_enter_data_dialog(self):
        if self.radio_btn_selling.isChecked():
            self.selling_enter_data_window_obj = SellingEnterDataDialogWindow()
            self.selling_enter_data_window_obj.retranslateUi(self.selling_enter_data_window_obj)
            self.selling_enter_data_window_obj.show()
        else:
            self.purchase_enter_data_window_obj = PurchaseEnterDataDialogWindow()
            self.purchase_enter_data_window_obj.retranslateUi(self.purchase_enter_data_window_obj)
            self.purchase_enter_data_window_obj.show()

    def pop_up_total_details(self):
        self.total_details_window_obj = TotalDetailsDialogWindow()
        self.total_details_window_obj.retranslateUi(self.total_details_window_obj)
        self.total_details_window_obj.show()


class LoginDialogWindow(QDialog, LogInDialog.Ui_LoginDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.main_dialog = None
        self.showErrorMessage = None

        self.btn_login.clicked.connect(self.get_password)

    def get_password(self):
        password = self.line_edit_password.text()

        if password == "1234":
            self.main_dialog = MainDialogWindow()
            self.main_dialog.retranslateUi(self.main_dialog)
            self.main_dialog.show()
            self.hide()
        else:
            self.showErrorMessage = QtWidgets.QErrorMessage()
            self.showErrorMessage.setWindowTitle("Error Message")
            self.showErrorMessage.showMessage("Incorrect Password!!! 😬")
            self.showErrorMessage.show()
            self.line_edit_password.clear()


class ViewStockDialogWindow(QDialog, ViewStockDialog.Ui_ViewStockDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        self.btn_ok.clicked.connect(self.hide)

        with open("data/Stock.csv", "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            rows = len(list(file_reader)) - 1

        self.tabel_widget_stock.setRowCount(rows)
        self.tabel_widget_stock.setColumnCount(2)

        stock = pd.read_csv("data/Stock.csv")

        dict_headers = {0: "Size", 1: "Qty"}

        self.tabel_widget_stock.setHorizontalHeaderLabels(["Size", "Quantity"])

        for i in range(rows):
            for j in dict_headers:
                self.value = str(stock.at[i, dict_headers[j]])
                self.tabel_widget_stock.setItem(i, j, QTableWidgetItem(self.value))


class SellingViewDataDialogWindow(QDialog, SellingViewDataDialog.Ui_SellingViewDataDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.showFullScreen()

        self.delete_data_obj = None

        self.btn_delete.clicked.connect(self.delete_record)
        self.btn_ok.clicked.connect(self.hide)

        with open("data/DataEntrySelling.csv", "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            rows = len(list(file_reader)) - 1

        self.table_widget_view_data.setRowCount(rows)
        self.table_widget_view_data.setColumnCount(13)

        selling_data_entry = pd.read_csv("data/DataEntrySelling.csv")

        dict_headers = {0: "Date", 1: "Party", 2: "GSM", 3: "Size", 4: "Qty", 5: "Rate", 6: "Payment+GST(12%)",
                        7: "Payment Date", 8: "Paid Amount", 9: "Cheque No.", 10: "Chalan No.",
                        11: "Remarks", 12: "Profit"}

        self.table_widget_view_data.setHorizontalHeaderLabels(["Date", "Party", "GSM", "Size", "Qty", "Rate",
                                                               "Payment+GST(12%)", "Payment Date", "Paid Amount",
                                                               "Cheque No.", "Chalan No.", "Remarks", "Profit"])

        for i in range(rows):
            for j in dict_headers:
                self.value = str(selling_data_entry.at[i, dict_headers[j]])
                self.table_widget_view_data.setItem(i, j, QTableWidgetItem(self.value))

    def delete_record(self):
        self.delete_data_obj = SellingDeleteDataDialogWindow()
        self.delete_data_obj.retranslateUi(self.delete_data_obj)
        self.delete_data_obj.show()


class SellingDeleteDataDialogWindow(QDialog, DeleteDataDialog.Ui_DeleteDataDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        self.index = None
        self.showErrorMessage = None
        self.file_of_selling = None
        self.file_of_stock = None
        self.deleted_stock = None
        self.existing_stock = None
        self.size = None
        self.dict_size_to_index = {36: 0, 44: 1, 48: 2, 54: 3, 58: 4, 60: 5, 63: 6}

        self.btn_delete.clicked.connect(self.delete_selected_record)
        self.btn_delete.clicked.connect(self.hide)

    def delete_selected_record(self):
        self.index = int(self.line_edit_index.text()) - 1

        with open("data/DataEntrySelling.csv", "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            rows = len(list(file_reader)) - 1

        self.file_of_selling = pd.read_csv("data/DataEntrySelling.csv")
        self.file_of_stock = pd.read_csv("data/Stock.csv")

        warnings.simplefilter(action="ignore", category=FutureWarning)

        self.deleted_stock = self.file_of_selling.at[self.index, "Qty"]
        self.size = self.file_of_selling.at[self.index, "Size"]
        self.existing_stock = self.file_of_stock.at[self.dict_size_to_index[self.size], "Qty"]

        self.file_of_stock.set_value(self.dict_size_to_index[self.size], "Qty",
                                     self.existing_stock + self.deleted_stock)
        self.file_of_stock.to_csv("data/Stock.csv", index=None)

        if self.index < rows:
            file = pd.read_csv("data/DataEntrySelling.csv")
            file.drop(file.index[self.index], inplace=True)
            file.to_csv("data/DataEntrySelling.csv", index=None)

            self.showErrorMessage = QtWidgets.QErrorMessage()
            self.showErrorMessage.setWindowTitle("Success Message")
            self.showErrorMessage.showMessage("Record deleted successfully!!! 😃")
            self.showErrorMessage.show()
        else:
            self.showErrorMessage = QtWidgets.QErrorMessage()
            self.showErrorMessage.setWindowTitle("Error Message")
            self.showErrorMessage.showMessage("Index out of bound!!! 😬")
            self.showErrorMessage.show()


class SellingEnterDataDialogWindow(QDialog, SellingEnterDataDialog.Ui_SellingEnterDataDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        self.dict_size_to_index = None
        self.file_data_entry = None
        self.date = None
        self.party_name = None
        self.gsm = None
        self.size = None
        self.selling_quantity = None
        self.selling_rate = None
        self.rate_of_44_size = None
        self.final_bill = None
        self.file_of_stock = None
        self.stock = None
        self.payment_paid_date = None
        self.paid_amount = None
        self.cheque_no = None
        self.chalan_no = None
        self.remarks = None
        self.purchase_rate = None
        self.table_price = None
        self.profit = None

        self.btn_add_record.clicked.connect(self.set_data)
        self.btn_add_record.clicked.connect(self.hide)
        self.btn_cancel.clicked.connect(self.hide)

    def set_data(self):
        self.dict_size_to_index = {36: 0, 44: 1, 48: 2, 54: 3, 58: 4, 60: 5, 63: 6}

        self.file_data_entry = open("data/DataEntrySelling.csv", "a+")
        self.date = self.date_edit_date.text()
        self.party_name = self.line_edit_party_name.text()
        self.gsm = int(self.combo_box_gsm.currentText())
        self.size = int(self.combo_box_size.currentText())
        self.selling_quantity = int(self.line_edit_qty.text())
        self.selling_rate = float(self.line_edit_selling_rate.text())
        self.rate_of_44_size = float(self.line_edit_purchase_rate_of_44_size.text())

        self.final_bill = round(((self.selling_rate * self.selling_quantity) +
                                 ((self.selling_rate * self.selling_quantity) * 12) / 100.0), 3)
        """
        To avoid FutureWarning (Basically raised at the time when we use df.set_value() method) in pandas I have written
        following statement and still if you don't get importance of the following line of code then feel 
        free to erase it!!! 
        """
        warnings.simplefilter(action="ignore", category=FutureWarning)

        self.file_of_stock = pd.read_csv("data/Stock.csv")
        self.stock = self.file_of_stock.at[self.dict_size_to_index[self.size], "Qty"]
        self.file_of_stock.set_value(self.dict_size_to_index[self.size], "Qty", self.stock - self.selling_quantity)
        self.file_of_stock.to_csv("data/Stock.csv", index=None)

        self.payment_paid_date = self.date_edit_payment_paid_date.text()
        self.paid_amount = float(self.line_edit_payment_paid_amount.text())
        self.cheque_no = self.line_edit_cheque_no.text()
        self.chalan_no = self.line_edit_chalan_no.text()
        self.remarks = self.text_edit_remarks.toPlainText()

        self.purchase_rate = round(((self.rate_of_44_size / 44) * self.size), 3)

        self.table_price = round(((self.selling_rate / 44) * self.size), 3)
        self.profit = round(((self.table_price - self.purchase_rate) * self.selling_quantity), 3)

        self.file_data_entry.write(
            self.date + "," + self.party_name + "," + str(self.gsm) + "," + str(self.size) + "," +
            str(self.selling_quantity) + "," + str(self.selling_rate) + "," + str(self.final_bill) + "," +
            self.payment_paid_date + "," + str(self.paid_amount) + "," + self.cheque_no + "," +
            self.chalan_no + "," + self.remarks + "," + str(self.profit) + "\n"
        )

        self.file_data_entry.close()


class TotalDetailsDialogWindow(QDialog, TotalDetailsDialog.Ui_TotalDetailsDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        self.btn_ok.clicked.connect(self.hide)

        with open("data/DataEntrySelling.csv", "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            rows = len(list(file_reader)) - 1

        self.profit_file = pd.read_csv("data/DataEntrySelling.csv")
        self.purchase_file = pd.read_csv("data/DataEntryPurchase.csv")

        total_profit, total_selling, total_purchase = 0, 0, 0
        for i in range(rows):
            total_profit += self.profit_file.at[i, "Profit"]
            total_selling += self.profit_file.at[i, "Payment+GST(12%)"]
            total_purchase += self.profit_file.at[i, "Payment+GST(12%)"]

        self.table_widget_total_details.setRowCount(3)
        self.table_widget_total_details.setColumnCount(2)

        self.table_widget_total_details.setHorizontalHeaderLabels(["Detail", "Rate"])

        self.table_widget_total_details.setItem(0, 0, QTableWidgetItem("Selling"))
        self.table_widget_total_details.setItem(1, 0, QTableWidgetItem("Purchase"))
        self.table_widget_total_details.setItem(2, 0, QTableWidgetItem("Profit"))

        self.table_widget_total_details.setItem(0, 1, QTableWidgetItem(str(total_selling)))
        self.table_widget_total_details.setItem(1, 1, QTableWidgetItem(str(total_purchase)))
        self.table_widget_total_details.setItem(2, 1, QTableWidgetItem(str(total_profit)))


class PurchaseEnterDataDialogWindow(QDialog, PurchaseEnterDataDialog.Ui_PurchaseEnterDataDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        self.dict_size_to_index = None
        self.file_data_entry = None
        self.date = None
        self.party_name = None
        self.gsm = None
        self.size = None
        self.purchase_quantity = None
        self.purchase_rate_entered_by_user = None
        self.rate_of_44_size = None
        self.final_bill = None
        self.file_of_stock = None
        self.stock = None
        self.payment_paid_date = None
        self.paid_amount = None
        self.cheque_no = None
        self.bill_no = None
        self.remarks = None
        self.purchase_rate = None
        self.table_price = None

        self.btn_add_record.clicked.connect(self.set_data)
        self.btn_add_record.clicked.connect(self.hide)
        self.btn_cancel.clicked.connect(self.hide)

    def set_data(self):
        self.dict_size_to_index = {36: 0, 44: 1, 48: 2, 54: 3, 58: 4, 60: 5, 63: 6}

        self.file_data_entry = open("data/DataEntryPurchase.csv", "a+")
        self.date = self.date_edit_date.text()
        self.party_name = self.line_edit_party_name.text()
        self.gsm = int(self.combo_box_gsm.currentText())
        self.size = int(self.combo_box_size.currentText())
        self.purchase_quantity = int(self.line_edit_qty.text())
        self.purchase_rate_entered_by_user = float(self.line_edit_selling_rate.text())
        self.rate_of_44_size = float(self.line_edit_purchase_rate_of_44_size.text())

        self.final_bill = round(((self.purchase_rate_entered_by_user * self.purchase_quantity) +
                                 ((self.purchase_rate_entered_by_user * self.purchase_quantity) * 12) / 100.0), 3)

        warnings.simplefilter(action="ignore", category=FutureWarning)

        self.file_of_stock = pd.read_csv("data/Stock.csv")
        self.stock = self.file_of_stock.at[self.dict_size_to_index[self.size], "Qty"]
        self.file_of_stock.set_value(self.dict_size_to_index[self.size], "Qty", self.stock + self.purchase_quantity)
        self.file_of_stock.to_csv("data/Stock.csv", index=None)

        self.payment_paid_date = self.date_edit_payment_paid_date.text()
        self.paid_amount = float(self.line_edit_payment_paid_amount.text())
        self.cheque_no = self.line_edit_cheque_no.text()
        self.bill_no = self.line_edit_chalan_no.text()
        self.remarks = self.text_edit_remarks.toPlainText()

        self.file_data_entry.write(
            self.date + "," + self.party_name + "," + str(self.gsm) + "," + str(self.size) + "," +
            str(self.purchase_quantity) + "," + str(self.purchase_rate_entered_by_user) + "," + str(self.final_bill)
            + "," + self.payment_paid_date + "," + str(self.paid_amount) + "," + self.cheque_no + "," +
            self.bill_no + "," + self.remarks + "\n"
        )

        self.file_data_entry.close()


class PurchaseViewDataDialogWindow(QDialog, SellingViewDataDialog.Ui_SellingViewDataDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.showFullScreen()

        self.delete_data_obj = None

        self.btn_delete.clicked.connect(self.delete_record)
        self.btn_ok.clicked.connect(self.hide)

        with open("data/DataEntryPurchase.csv", "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            rows = len(list(file_reader)) - 1

        self.table_widget_view_data.setRowCount(rows)
        self.table_widget_view_data.setColumnCount(12)

        purchase_data_entry = pd.read_csv("data/DataEntryPurchase.csv")

        dict_headers = {0: "Date", 1: "Party", 2: "GSM", 3: "Size", 4: "Qty", 5: "Rate", 6: "Payment+GST(12%)",
                        7: "Payment Date", 8: "Paid Amount", 9: "Cheque No.", 10: "Bill No.",
                        11: "Remarks"}

        self.table_widget_view_data.setHorizontalHeaderLabels(["Date", "Party", "GSM", "Size", "Qty", "Rate",
                                                               "Payment+GST(12%)", "Payment Date", "Paid Amount",
                                                               "Cheque No.", "Bill No.", "Remarks"])

        for i in range(rows):
            for j in dict_headers:
                self.value = str(purchase_data_entry.at[i, dict_headers[j]])
                self.table_widget_view_data.setItem(i, j, QTableWidgetItem(self.value))

    def delete_record(self):
        self.delete_data_obj = PurchaseDeleteDataDialogWindow()
        self.delete_data_obj.retranslateUi(self.delete_data_obj)
        self.delete_data_obj.show()


class PurchaseDeleteDataDialogWindow(QDialog, DeleteDataDialog.Ui_DeleteDataDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.show()

        self.index = None
        self.showErrorMessage = None
        self.file_of_purchase = None
        self.file_of_stock = None
        self.deleted_stock = None
        self.existing_stock = None
        self.size = None

        self.dict_size_to_index = {36: 0, 44: 1, 48: 2, 54: 3, 58: 4, 60: 5, 63: 6}

        self.btn_delete.clicked.connect(self.delete_selected_record)
        self.btn_delete.clicked.connect(self.hide)

    def delete_selected_record(self):
        self.index = int(self.line_edit_index.text()) - 1

        with open("data/DataEntryPurchase.csv", "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            rows = len(list(file_reader)) - 1

        self.file_of_purchase = pd.read_csv("data/DataEntryPurchase.csv")
        self.file_of_stock = pd.read_csv("data/Stock.csv")

        warnings.simplefilter(action="ignore", category=FutureWarning)

        self.deleted_stock = self.file_of_purchase.at[self.index, "Qty"]
        self.size = self.file_of_purchase.at[self.index, "Size"]
        self.existing_stock = self.file_of_stock.at[self.dict_size_to_index[self.size], "Qty"]

        self.file_of_stock.set_value(self.dict_size_to_index[self.size], "Qty",
                                     self.existing_stock - self.deleted_stock)
        self.file_of_stock.to_csv("data/Stock.csv", index=None)

        if self.index < rows:
            file = pd.read_csv("data/DataEntryPurchase.csv")
            file.drop(file.index[self.index], inplace=True)
            file.to_csv("data/DataEntryPurchase.csv", index=None)

            self.showErrorMessage = QtWidgets.QErrorMessage()
            self.showErrorMessage.setWindowTitle("Success Message")
            self.showErrorMessage.showMessage("Record deleted successfully!!! 😃")
            self.showErrorMessage.show()
        else:
            self.showErrorMessage = QtWidgets.QErrorMessage()
            self.showErrorMessage.setWindowTitle("Error Message")
            self.showErrorMessage.showMessage("Index out of bound!!! 😬")
            self.showErrorMessage.show()


application = QApplication(sys.argv)
login_screen = LoginDialogWindow()
login_screen.show()
application.exec_()
