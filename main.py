"""Data Entry desktop app for Fine Enterprise"""

import sys
import pandas as pd
import csv
import warnings

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui

import MainDialog
import LogInDialog
import SellingEnterDataDialog
import SellingViewDataDialog
import ViewStockDialog


class MainDialogWindow(QDialog, MainDialog.Ui_MainDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.view_stock_window_obj = None
        self.selling_enter_data_window_obj = None
        self.selling_view_data_window_obj = None

        self.btn_enter_data.hide()
        self.btn_view_data.hide()
        self.btn_delete_data.hide()
        self.btn_view_graph.hide()

        self.btn_stock.clicked.connect(self.pop_up_stock_dialog)
        self.btn_enter_data.clicked.connect(self.pop_up_selling_enter_data_dialog)
        self.btn_view_data.clicked.connect(self.pop_up_selling_view_data_dialog)

    def pop_up_stock_dialog(self):
        self.view_stock_window_obj = ViewStockDialogWindow()
        self.view_stock_window_obj.retranslateUi(self.view_stock_window_obj)
        self.view_stock_window_obj.show()

    def pop_up_selling_view_data_dialog(self):
        if self.radio_btn_selling.isChecked():
            self.selling_view_data_window_obj = SellingViewDataDialogWindow()
            self.selling_view_data_window_obj.retranslateUi(self.selling_view_data_window_obj)
            self.selling_view_data_window_obj.show()
        else:
            pass

    def pop_up_selling_enter_data_dialog(self):
        if self.radio_btn_selling.isChecked():
            self.selling_enter_data_window_obj = SellingEnterDataDialogWindow()
            self.selling_enter_data_window_obj.retranslateUi(self.selling_enter_data_window_obj)
            self.selling_enter_data_window_obj.show()
        else:
            pass


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
            self.showErrorMessage.showMessage("Incorrect Password!!!")
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


class SellingViewDataDialogWindow(QDialog, SellingViewDataDialog.Ui_SellingViewData):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.showFullScreen()

        self.btn_ok.clicked.connect(self.hide)

        with open("data/DataEntrySelling.csv", "r") as file:
            file_reader = csv.reader(file, delimiter=",")
            rows = len(list(file_reader)) - 1

        self.table_widget_view_data.setColumnWidth(0, 1)

        self.table_widget_view_data.setRowCount(rows)
        self.table_widget_view_data.setColumnCount(13)

        selling_data_entry = pd.read_csv("data/DataEntrySelling.csv")

        dict_headers = {0: "Date", 1: "Party", 2: "GSM", 3: "Size", 4: "Qty", 5: "Rate", 6: "Payment+GST(12%)",
                        7: "Payment Date", 8: "Paid Amount", 9: "Cheque No.", 10: "Chalan No.",
                        11: "Remarks", 12: "Profit"}

        self.table_widget_view_data.setHorizontalHeaderLabels(["Date", "Party", "GSM", "Size", "Qty", "Rate",
                                                               "Payment+GST(12%)",
                                                               "Payment Date", "Paid Amount", "Cheque No.",
                                                               "Chalan No.", "Remarks", "Profit"])

        for i in range(rows):
            for j in dict_headers:
                self.value = str(selling_data_entry.at[i, dict_headers[j]])
                self.table_widget_view_data.setItem(i, j, QTableWidgetItem(self.value))


class SellingEnterDataDialogWindow(QDialog, SellingEnterDataDialog.Ui_EnterDataDialog):
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

        self.final_bill = (self.selling_rate * self.selling_quantity) + \
                          ((self.selling_rate * self.selling_quantity) * 12) / 100.0

        # To avoid FutureWarning in pandas I have written following statement and still
        # If you don't get importance of the following line of code then feel free to erase it!!!
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

        self.purchase_rate = (self.rate_of_44_size / 44) * self.size

        self.table_price = (self.selling_rate / 44) * self.size
        self.profit = (self.table_price - self.purchase_rate) * self.selling_quantity

        self.file_data_entry.write(
            self.date + "," + self.party_name + "," + str(self.gsm) + "," + str(self.size) + "," +
            str(self.selling_quantity) + "," + str(self.selling_rate) + "," + str(self.final_bill) + "," +
            self.payment_paid_date + "," + str(self.paid_amount) + "," + self.cheque_no + "," +
            self.chalan_no + "," + self.remarks + "," + str(self.profit) + "\n"
        )

        self.file_data_entry.close()


application = QApplication(sys.argv)
login_screen = LoginDialogWindow()
login_screen.show()
application.exec_()


"""
dict_size_to_index = {36: 0, 44: 1, 48: 2, 54: 3, 58: 4, 60: 5, 63: 6}


def purchase():
    file_data_entry = open("data/DataEntryPurchase.csv", "a+")
    date = input("Date: ")
    party_name = input("Party name: ")
    gsm = int(input("GSM: "))
    size = int(input("Size: "))
    purchase_quantity = int(input("Quantity: "))
    rate_of_44_size = float(input("Purchase rate of 44 size: "))

    purchase_rate = (rate_of_44_size / 44) * size

    file_of_stock = pd.read_csv("data/Stock.csv")
    stock = file_of_stock.at[dict_size_to_index[size], "Qty"]
    file_of_stock.set_value(dict_size_to_index[size], "Qty", stock + purchase_quantity)
    file_of_stock.to_csv("data/Stock.csv", index=None)

    final_bill = (purchase_rate * purchase_quantity) + (((purchase_rate * purchase_quantity) * 12) / 100.0)

    payment_paid_date = input("Payment paid date: ")
    paid_amount = float(input("Paid amount: "))
    cheque_no = input("Cheque No.: ")
    bill_no = input("Bill No.: ")
    remarks = input("Remarks: ")

    file_data_entry.write(
        date + "," + party_name + "," + str(gsm) + "," + str(size) + "," + str(purchase_quantity) + "," +
        str(purchase_rate) + "," + str(final_bill) + "," + party_name + "," + payment_paid_date + "," + str(paid_amount)
        + "," + cheque_no + "," + bill_no + "," + remarks + "\n"
    )
    file_data_entry.close()


if __name__ == "__main__":
    pwd = "MMS8050"
    passWord = input("Password: ")
    if passWord == pwd:
        print("Logged in successfully!!!\n")

        while True:
            choice = int(input("1.Enter Data\n2.View Data\n3.Delete Data\n4.Exit\n\nEnter your choice: "))

            if choice == 1:
                selling_or_purchase = int(input("\n1.Enter Selling Data\n2.Enter Purchase Data\n\nEnter your choice: "))
                if selling_or_purchase == 1:
                    selling()
                    response = input("\nPress any key to continue....")
                    continue

                elif selling_or_purchase == 2:
                    purchase()
                    response = input("\nPress any key to continue....")
                    continue

                else:
                    print("\nInvalid choice!!!\nPlease enter valid choice!!!\n")
                    response = input("\nPress any key to continue....")
                    continue

            elif choice == 2:
                selling_or_purchase = int(input("\n1.View Selling Data\n2.View Purchase Data\n\nEnter your choice: "))
                if selling_or_purchase == 1:
                    view_selling_data()
                    response = input("\nPress any key to continue....")
                    continue

                elif selling_or_purchase == 2:
                    view_purchase_data()
                    response = input("\nPress any key to continue....")
                    continue

                else:
                    print("\nInvalid choice!!!\nPlease enter valid choice!!!\n")
                    response = input("\nPress any key to continue....")
                    continue

            elif choice == 3:
                selling_or_purchase = int(input("\n1.Delete Selling Data\n2.Delete Purchase Data\n\nEnter your choice: "))
                if selling_or_purchase == 1:
                    view_selling_data()
                    index = int(input("Enter index number: "))
                    df = pd.read_csv("data/DataEntrySelling.csv")
                    df.drop(df.index[index], inplace=True)
                    df.to_csv("data/DataEntrySelling.csv", index=None)
                    response = input("\nPress any key to continue....")
                    continue

                elif selling_or_purchase == 2:
                    view_purchase_data()
                    index = int(input("Enter index number: "))
                    df = pd.read_csv("data/DataEntryPurchase.csv")
                    df.drop(df.index[index], inplace=True)
                    df.to_csv("data/DataEntryPurchase.csv", index=None)
                    response = input("\nPress any key to continue....")
                    continue

                else:
                    print("\nInvalid choice!!!\nPlease enter valid choice!!!\n")
                    response = input("\nPress any key to continue....")
                    continue

            elif choice == 4:
                exit(0)

            else:
                print("\nInvalid choice!!!\nPlease enter valid choice!!!\n")

    else:
        print("Permission denied!!!\nEnter correct password!!!\n")"""
