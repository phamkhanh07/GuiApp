import sys
from os.path import expanduser as ospath
import xlrd
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog, QInputDialog, QErrorMessage
from PyQt5 import QtGui, QtCore
from numpy import unicode

from app import Ui_DomainCreate
import unicodedata
import pandas as pd
from PandaModel import PandasModel
from getUser import get_user
import dosmt


class AppWindows(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DomainCreate()
        self.ui.setupUi(self)

        self.file_Path = None  # file excel path

        # Button Quit
        self.ui.btn_Quit.clicked.connect(self.close)

        # Button help
        self.ui.btn_help.clicked.connect(self.show_Dialogs)

        # button get user domain
        self.ui.btn_GetDomainUser.clicked.connect(self.getDomainUer)

        # Button open file
        self.ui.btn_OpenFile.clicked.connect(self.open_FileClicked)

        # Button create user
        # self.ui.btn_CreateNewUser.colorCount(self.create_User)

        self.show()

    # Open file dialog
    def open_FileClicked(self):
        # fn = self.setOpenFileName()[0]
        self.file_Path = self.set_OpenFileName()
        fn = self.file_Path[0]
        if dosmt.is_Excel(fn) == True:
            df = pd.read_excel(fn)
            model = PandasModel(df)
            self.ui.tbt_View.setModel(model)
            self.do = True
            self.update()
        else:
            mess = QErrorMessage(self)
            mess.setWindowTitle("Notice!!")
            mess.showMessage("Open Excel file only")

    def set_OpenFileName(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open Excel file', filter='*.xls, *xlsx')
        return fileName

    # create user:
    def create_User(self):
        # get domain user
        l = dosmt.read_User()
        c_UserName = []
        c_Company = []
        c_Dep = []
        c_Mobile = []

        # user temp
        df = pd.read_excel(self.file_Path[0])
        temp_Name = df['name'].tolist()
        temp_Company = df['company'].tolist()
        temp_Dep = df['department'].tolist()
        temp_Mobile = df['mobile'].tolist()

        for c in temp_Company:
            c_Company.append(dosmt.company_name(c))
        for n in temp_Name:
            c_UserName.append(dosmt.user_Creater(n))

    # get in for from excel file
    def get_Info(self, path):
        if self.do:
            fn = self.setOpenFileName()[0]
            df = pd.read_excel(fn)

    def show_Dialogs(self):
        help_text = '''
        Step to check:
            1: Press Get Domain user button
            2: Copy and paste user information from HR to table
            3: press button check 
            4: Export new excel file
        '''
        dialog = QMessageBox()
        dialog.setWindowTitle("User Guide")
        dialog.setText(help_text)
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppWindows()
    sys.exit(app.exec_())
