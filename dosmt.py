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
def user_creator(s, l):
    temp_user = user_maker(no_accent(s).lower())
    if temp_user not in l:
        user_domain = temp_user
        return user_domain
    else:
        user_domain = add_number(temp_user, l)
        return user_domain


# show error


# remove vietnamese accent
def no_accent(s):
    s = s.encode('utf-8').decode('utf-8')
    s = re.sub(u'Đ', 'D', s)
    s = re.sub(u'đ', 'd', s)
    return (unicodedata.normalize('NFKD', str(s)).encode('ASCII', 'ignore')).decode('utf-8')


# Check file is Excel file
def is_excel(path):
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


# this list will updating
# make department name
def map_name(dept_name):
    path = os.getcwd() + r"\Departments.xlsx"
    if not path:
        print('File not exist!')
    else:
        df = pd.read_excel(path)
        find = df.loc[df['Phòng'].lower() == dept_name.lower()]
        sort_name = find['Viết tắt'].values[0]
        return sort_name


# read user from json to list
def read_user():
    user_list = []
    file_Path = os.getcwd() + r"\DUMP\domain_users.json"
    if file_Path:
        if 'DUMP' in os.listdir(os.getcwd()):
            data = pd.read_json(file_Path)
            cl = data.loc[:, 'attributes']
            for line in cl:
                user_list.append(str(line['sAMAccountName']).replace("'", "").replace("[", "").replace("]", ""))
        return user_list
    else:
        print('file not exist!')


# add number to user when user in list
def add_number(s, l):
    n = 1
    while s in l:
        n += 1
        name = s.split('.')[0] + str(n) + '.' + s.split('.')[1]
        if name not in l:
            name = s.split('.')[0] + str(n) + '.' + s.split('.')[1]
            return name


def add_mail(s):
    if s:
        s = s + '@hawee.com.vn'
        return s
    else:
        return None


# create new user flow company name format
def user_maker(srt_name):
    # srt is full name, lower and no accent
    converted_name = []
    list_str = srt_name.split()

    if len(list_str) <= 2:
        first_name = list_str[-1]
        last_name = list_str[0]
        converted_name.clear()
        converted_name.insert(0, first_name)
        converted_name.insert(1, '.')
        converted_name.insert(2, last_name)
        name = ''.join(str(x) for x in converted_name)
        return name
    else:
        if str(list_str[-1]) == 'anh':
            first_name = list_str[-1]
            mid_name = list_str[-2]
            last_name = list_str[0]
            converted_name.clear()
            converted_name.insert(1, first_name)
            converted_name.insert(0, mid_name)
            converted_name.insert(2, '.')
            converted_name.insert(3, last_name)
            name = ''.join(str(x) for x in converted_name)
            return name
        else:
            first_name = list_str[-1]
            last_name = list_str[0]
            mid_name = list_str[1]
            converted_name.clear()
            converted_name.insert(0, first_name)
            converted_name.insert(1, '.')
            converted_name.insert(3, mid_name)
            converted_name.insert(2, last_name)
            name = ''.join(str(x) for x in converted_name)
            return name
