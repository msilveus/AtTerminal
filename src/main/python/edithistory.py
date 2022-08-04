from PyQt5 import QtCore, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget

import config_utils
from edit_history import Ui_EditHistory

class EditHistory(QWidget, Ui_EditHistory):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.setupUi(self)
        self.properties = config_utils.read_config()

        self.mainwindow = mainwindow
        self.btnAdd.clicked.connect(self.onAddHistory)
        self.bntUpdate.clicked.connect(self.onUpdateHistory)
        self.btnDelete.clicked.connect(self.onDeleteHistory)
        self.btnSort.clicked.connect(self.onSort)
        self.btnSave.clicked.connect(self.onSaveHistory)
        self.btnExit.clicked.connect(self.onExit)
        self.listView.clicked.connect(self.onItemSelected)
        self.lineEdit.returnPressed.connect(self.onAddHistory)

        self.model = QStandardItemModel(self.listView)
        
        numOfitems = self.mainwindow.historyBox.count()
        for index in range(numOfitems):
            cmd = self.mainwindow.historyBox.itemText(index)
            item = QStandardItem(cmd)
            item.setCheckable(True)
            self.model.appendRow(item)
            
        self.listView.setModel(self.model)
        
        self.set_night_mode(self.mainwindow.nightmode)

    def onAddHistory(self):
        self.currentIndex = self.listView.currentIndex()
        cmd = self.lineEdit.text()
        item = QStandardItem(cmd)
        item.setCheckable(True)
        self.model.appendRow(item)
        self.listView.setModel(self.model)
        self.lineEdit.setText("")

    def onUpdateHistory(self):
        self.currentIndex = self.listView.currentIndex()
        cmd = self.lineEdit.text()
        item = QStandardItem(cmd)
        item.setCheckable(True)
        self.model.setItem(self.currentIndex.row(), self.currentIndex.column(), item)
        self.listView.setModel(self.model)

    def onDeleteHistory(self):
        items2Remove = list()
        model = self.listView.model()
        for row in range(model.rowCount()):
            item = model.item(row)
            if item.isCheckable() and item.checkState() == QtCore.Qt.Checked:
                index = model.index(row, 0)
                items2Remove.insert(0,index)
        for index in items2Remove:
            model.removeRow(index.row())
            
    def onSaveHistory(self):
        self.doUpdate(True)
        self.close()

    def onExit(self):
        self.doUpdate(False)
        self.close()

    def onItemSelected(self):
        self.currentIndex = self.listView.currentIndex()
        cmd = self.currentIndex.data()
        self.lineEdit.setText(cmd)

    def set_night_mode(self, nightmode=False):
        self.properties = config_utils.read_config()
        print(self.properties)
        try:
            if 'font' in self.properties and self.properties['font']:
                font = self.properties['font']
        except Exception as e:
            font = "Times"
        try:
            if 'font_size' in self.properties and self.properties['font_size']:
                font_size = self.properties['font_size']
        except Exception as e:
            font_size = 12
        if nightmode:
            self.setStyleSheet(
                "background-color: rgb(162, 0, 0); color: rgb(200, 200, 200);" + "font: {}pt \"{}\";".format(font_size,
                                                                                                             font))
        else:
            self.setStyleSheet(
                "background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);" + "font: {}pt \"{}\";".format(font_size,
                                                                                                           font))

    def doUpdate(self, save=False):
        if save:
            cmdlist = dict()
        numOfItems = self.mainwindow.historyBox.count()
        for index in range(numOfItems):
            self.mainwindow.historyBox.removeItem(0)
        model = self.listView.model()
        for row in range(model.rowCount()):
            index = model.index(row, 0)
            cmd = model.itemData(index)
            self.mainwindow.historyBox.addItem(cmd[0])
            if save:
                cmdlist.update({str(row): cmd[0]})
    
        if save:
            config_utils.save_history(cmdlist)

    def onSort(self):
        self.listView.model().sort(0)

