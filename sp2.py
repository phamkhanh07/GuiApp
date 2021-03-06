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


def userMacker(srt_Name):
    # srt is full name, lower and no accent
    converted_name = []
    list_Str = srt_Name.split()

    if len(list_Str) <= 2:
        first_Name = list_Str[-1]
        last_Name = list_Str[0]
        converted_name.clear()
        converted_name.insert(0, first_Name)
        converted_name.insert(1, '.')
        converted_name.insert(2, last_Name)
        name = ''.join(str(x) for x in converted_name)
        return name
    else:
        if str(list_Str[-1]) == 'anh':
            first_Name = list_Str[-1]
            mid_name = list_Str[-2]
            last_Name = list_Str[0]
            converted_name.clear()
            converted_name.insert(1, first_Name)
            converted_name.insert(0, mid_name)
            converted_name.insert(2, '.')
            converted_name.insert(3, last_Name)
            name = ''.join(str(x) for x in converted_name)
            return name
        else:
            first_Name = list_Str[-1]
            last_Name = list_Str[0]
            mid_name = list_Str[1]
            converted_name.clear()
            converted_name.insert(0, first_Name)
            converted_name.insert(1, '.')
            converted_name.insert(3, mid_name)
            converted_name.insert(2, last_Name)
            name = ''.join(str(x) for x in converted_name)
            return name
