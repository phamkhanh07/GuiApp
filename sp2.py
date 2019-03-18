from PyQt5.QtWidgets import QDialog, QProgressBar, QLabel, QHBoxLayout
from PyQt5.QtCore import pyqtSlot


class ProcessBar_Dialog(QDialog):
    def __init__(self):
        super(ProcessBar_Dialog, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.progressLabel = QLabel("process Bar:", self)
        self.processBar = QProgressBar(self)
        self.processBar.setMaximum(100)
        self.processBar.setMinimum(0)

        self.hboxLayout = QHBoxLayout(self)

        self.hboxLayout.addWidget(self.progressLabel)
        self.hboxLayout.addWidget(self.processBar)
        self.show()
