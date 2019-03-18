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

        # Button Quit
        self.ui.btn_Quit.clicked.connect(self.close)

        # Button help
        self.ui.btn_help.clicked.connect(self.showDialogs)

        # button get user domain
        self.ui.btn_GetDomainUser.clicked.connect(self.getDomainUer)

        # Button open file
        self.ui.btn_OpenFile.clicked.connect(self.selectedFile())

        # Button create user
        self.ui.btn_CreateNewUser.colorCount(self.create_User)

        self.show()

    # Open file dialog
    def openExcel(self):
        # fn = filename[0]
        fb = selectedFile()
        if dosmt.is_Excel(fn) == True:
            df = pd.read_excel(fn)
            model = PandasModel(df)
            self.ui.tbt_View.setModel(model)
        else:
            mess = QErrorMessage(self)
            mess.setWindowTitle("Notice!!")
            mess.showMessage("Open Excel file only")

    def selectedFile(self):
        option = QFileDialog.options()
        option |= QFileDialog.DontUseNativeDialog
        filename = QFileDialog.getOpenFileNames(self, "Select file", "", "Excel files(.xlsx, .xls)")
        self.ui.btn_OpenFile = filename
        return filename

    # get Domain user
    def getDomainUer(self):
        get_user()

    # Create new user
    def create_User(self):
        user = []  #

    def showDialogs(self):
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
