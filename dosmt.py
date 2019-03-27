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


# create user domain
def user_Creater(s, l):
    temp_User = user_Maker(no_accent(s).lower())
    if temp_User not in l:
        user_Domain = temp_User
        return user_Domain
    else:
        user_Domain = add_Number(temp_User, l)
        return user_Domain


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


# run window command
def run_CMD(cmd):
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


# make department name
def departmant_Name(s):
    return None


# read user from json to list
def read_User():
    user_list = []
    file_Path = os.getcwd() + r"\DUMP\domain_users.json"
    if 'DUMP' in os.listdir(os.getcwd()):
        data = pd.read_json(file_Path)
        cl = data.loc[:, 'attributes']
        for line in cl:
            user_list.append(str(line['sAMAccountName']).replace("'", "").replace("[", "").replace("]", ""))
    return user_list


# add number to user when user in list
def add_Number(s, l):
    n = 1
    while s in l:
        n += 1
        name = s.split('.')[0] + str(n) + '.' + s.split('.')[1]
        if name not in l:
            name = s.split('.')[0] + str(n) + '.' + s.split('.')[1]
            return name
            break


# create new user flow company name format
def user_Maker(srt_Name):
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
