import os
import shutil
import subprocess
import pandas as pd
import dosmt

user_list = []
json_path = os.getcwd() + "\\DUMP\\" + 'domain_users.json'
cmd = '''python -m ldapdomaindump -u "hawee.local\\admin.khanhpn2" -p Ph@mkhanh07 -d "-" -o DUMP --no-html --no-grep -m hawee.local'''


def get_user():
    if 'DUMP' in os.listdir(os.getcwd()):
        dosmt.rm_folder('DUMP')
        dosmt.run_cmd(cmd)
    else:
        dosmt.run_cmd(cmd)