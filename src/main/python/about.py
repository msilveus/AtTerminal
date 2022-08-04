from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QWidget

import config_utils
from about_window import Ui_aboutBox

class AboutBox(QWidget, Ui_aboutBox):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.version = "2.0.3"

        self.btnOK.clicked.connect(self.close)
        self.lblAbout.setText("AtTerminal v{}".format(self.version))
        self.lblAuthor.setText("Authors:\nSam Ahrar & Michael Silveus")

