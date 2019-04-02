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
        self.file_name = None  # dataframe

        # Button Quit
        self.ui.btn_Quit.clicked.connect(self.close)

        # Button help
        self.ui.btn_help.clicked.connect(self.show_Dialogs)

        # button get user domain
        # self.ui.btn_GetDomainUser.clicked.connect(self.getDomainUer)

        # Button open file
        self.ui.btn_OpenFile.clicked.connect(self.open_FileClicked)

        # Button create user
        self.ui.btn_CreateNewUser.clicked.connect(self.crear_user_domain)

        self.show()

    # Open file dialog
    def open_FileClicked(self):
        # fn = self.setOpenFileName()[0]
        self.file_Path = self.set_OpenFileName()
        self.file_name = self.file_Path[0]
        if dosmt.is_excel(self.file_name) == True:
            df = pd.read_excel(self.file_name)
            self.load_df(df)
        else:
            mess = QErrorMessage(self)
            mess.setWindowTitle("Notice!!")
            mess.showMessage("Open Excel file only")

    def set_OpenFileName(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open Excel file', filter='*.xls, *xlsx')
        return fileName

    # create domain user
    def crear_user_domain(self):
        user_domain= dosmt.read_user()
        new_userdomain = []
        new_email = []
        df = pd.read_excel(self.file_name)
        for u in df['name']:
            new_userdomain.append(dosmt.add_number(dosmt.user_maker(dosmt.no_accent(u).lower()), user_domain))
        df['User Domain'] = new_userdomain
        for u in new_userdomain:
            new_email.append(dosmt.add_mail(u))
        df['Email'] = new_email
        self.load_df(df)


    # load df tbt_View:
    def load_df(self, df):
        mode = PandasModel(df)
        self.ui.tbt_View.setModel(mode)
        self.do = True
        self.update()

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
