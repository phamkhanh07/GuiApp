# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DomainCreate(object):
    def setupUi(self, DomainCreate):
        DomainCreate.setObjectName("DomainCreate")
        DomainCreate.resize(912, 620)
        self.tbt_View = QtWidgets.QTableView(DomainCreate)
        self.tbt_View.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.tbt_View.setObjectName("tbt_View")
        #self.tbt_View.setColumnCount(0)
        #self.tbt_View.setRowCount(0)
        self.btn_GetDomainUser = QtWidgets.QPushButton(DomainCreate)
        self.btn_GetDomainUser.setGeometry(QtCore.QRect(800, 360, 101, 23))
        self.btn_GetDomainUser.setMinimumSize(QtCore.QSize(101, 23))
        self.btn_GetDomainUser.setObjectName("btn_GetDomainUser")
        self.btn_CreateNewUser = QtWidgets.QPushButton(DomainCreate)
        self.btn_CreateNewUser.setGeometry(QtCore.QRect(800, 410, 101, 23))
        self.btn_CreateNewUser.setMinimumSize(QtCore.QSize(91, 23))
        self.btn_CreateNewUser.setObjectName("btn_CreateNewUser")
        self.btn_Quit = QtWidgets.QPushButton(DomainCreate)
        self.btn_Quit.setGeometry(QtCore.QRect(800, 510, 101, 23))
        self.btn_Quit.setObjectName("btn_Quit")
        self.btn_help = QtWidgets.QPushButton(DomainCreate)
        self.btn_help.setGeometry(QtCore.QRect(800, 560, 101, 23))
        self.btn_help.setObjectName("btn_help")
        self.btn_Export = QtWidgets.QPushButton(DomainCreate)
        self.btn_Export.setGeometry(QtCore.QRect(800, 460, 101, 23))
        self.btn_Export.setObjectName("btn_Export")
        self.progressBar = QtWidgets.QProgressBar(DomainCreate)
        self.progressBar.setGeometry(QtCore.QRect(10, 590, 891, 21))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setObjectName("progressBar")
        self.btn_OpenFile = QtWidgets.QPushButton(DomainCreate)
        self.btn_OpenFile.setGeometry(QtCore.QRect(800, 310, 101, 23))
        self.btn_OpenFile.setObjectName("btn_OpenFile")

        self.retranslateUi(DomainCreate)
        QtCore.QMetaObject.connectSlotsByName(DomainCreate)
        DomainCreate.setTabOrder(self.tbt_View, self.btn_GetDomainUser)
        DomainCreate.setTabOrder(self.btn_GetDomainUser, self.btn_CreateNewUser)
        DomainCreate.setTabOrder(self.btn_CreateNewUser, self.btn_Export)
        DomainCreate.setTabOrder(self.btn_Export, self.btn_Quit)
        DomainCreate.setTabOrder(self.btn_Quit, self.btn_help)

    def retranslateUi(self, DomainCreate):
        _translate = QtCore.QCoreApplication.translate
        DomainCreate.setWindowTitle(_translate("DomainCreate", "Dialog"))
        self.btn_GetDomainUser.setText(_translate("DomainCreate", "Get Domain Users"))
        self.btn_CreateNewUser.setText(_translate("DomainCreate", "Create New User"))
        self.btn_Quit.setText(_translate("DomainCreate", "Quit"))
        self.btn_help.setText(_translate("DomainCreate", "Help"))
        self.btn_Export.setText(_translate("DomainCreate", "Export"))
        self.btn_OpenFile.setText(_translate("DomainCreate", "Open File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DomainCreate = QtWidgets.QDialog()
    ui = Ui_DomainCreate()
    ui.setupUi(DomainCreate)
    DomainCreate.show()
    sys.exit(app.exec_())

