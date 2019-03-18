import re
import unicodedata
import os
import shutil
import subprocess
from pathlib import Path
from PyQt5.uic.properties import QtWidgets
from openpyxl import load_workbook
import pandas as pd
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5 import QtGui, QtCore


# remove vietnamese accent
def no_accent(s):
    s = s.encode('utf-8').decode('utf-8')
    s = re.sub(u'Đ', 'D', s)
    s = re.sub(u'đ', 'd', s)
    return (unicodedata.normalize('NFKD', str(s)).encode('ASCII', 'ignore')).decode('utf-8')


# Check file is Excel file
def is_Excel(path):
    suff = Path(path).suffix
    if suff == '.xlsx' or suff == '.xls':
        return True
    else:
        return False


# remove folder
def rm_folder(name):
    folders = os.listdir(os.getcwd())
    if name in folders:
        shutil.rmtree(name)
    else:
        print("Error")


# remove file in folder
def rm_file(file):
    if os.path.exists(file):
        os.remove(file)
    else:
        print("file does not exist")


# open excel. csv files


# run window command
def run_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)


# make company name
def company_name(s):
    if s == 'HWIDC':
        return "Hawee.IDC"
    if s == "HWPT":
        return "Hawee.PT"
    if s == "HWME":
        return "Hawee.ME"
    else:
        return "Check Company name!"


# read user from json to list

def read_user(path):
    user_list = []
    if 'DUMP' in os.listdir(os.getcwd()):
        data = pd.read_json(path)
        cl = data.loc[:, 'attributes']
        for line in cl:
            user_list.append(line['sAMAccountName'])
    return user_list
