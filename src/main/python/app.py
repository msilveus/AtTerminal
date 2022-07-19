from PyQt5 import QtGui, QtCore

import selectport
from PyQt5.QtWidgets import QMainWindow

from edithistory import EditHistory
from main_window import Ui_MainWindow
import config_utils

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.properties = config_utils.read_config()

        self.actionConfiguration.triggered.connect(self.onShowSetup)
        self.actionHistory.triggered.connect(self.onEditHistory)
        self.actionExit.triggered.connect(self.onActionExit)
        self.sendEdit.returnPressed.connect(self.onSendData)
        self.btnSend.clicked.connect(self.onSendData)
        self.btnSendHistory.clicked.connect(self.onSendHistory)
        self.actionAutoScroll.triggered.connect(self.onAutoScroll)
        self.viewPort.setReadOnly(True)
        self.viewPort.verticalScrollBar().setVisible(True)
        self.viewPort.verticalScrollBar().valueChanged.connect(self.onScrollEvent)
        self.actionSuspend_Comm_Port.triggered.connect(self.handle_disconnect_resume)
        
        self.stopsign = QtGui.QIcon()
        self.stopsign.addPixmap(QtGui.QPixmap("images/stop-sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logicon = QtGui.QIcon()
        self.logicon.addPixmap(QtGui.QPixmap("images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.serialClass = None
        self.port_settings = None
        self.nightmode = False
        
    def onShowSetup(self):
        if (self.serialClass != None):
            self.serialClass.shutdown_serial()
        self.list_of_window = list()
        self.port_settings = selectport.SelectPort(self)
        self.list_of_window.append(self.port_settings)
        self.port_settings.show()
    
    def onActionExit(self):
        self.close()
    
    def closeEvent(self, event):
        self.onActionExit()
    
    def onSendData(self):
        cmd = self.sendEdit.text()
        self.sendEdit.clear()
        self.historyBox.addItem(cmd)
        if (self.serialClass != None):
            nbytes = self.serialClass.send_to_uart(cmd + "\r\n")
        else:
            self.viewPort.append("Comm port not setup")
    
    def onSendHistory(self):
        cmd = self.historyBox.currentText()
        if (self.serialClass != None):
            nbytes = self.serialClass.send_to_uart(cmd + "\r\n")
        else:
            self.viewPort.append("Comm port not setup")
    
    def onAutoScroll(self):
        if (self.autoscroll):
            self.autoscroll = False
        else:
            self.autoscroll = True
        
        if not self.autoscroll:
            bottom = self.viewPort.verticalScrollBar().maximum() - 10
            self.viewPort.verticalScrollBar().setSliderPosition(bottom)
    
    def onScrollEvent(self):
        self.autoscroll = False
        position = self.viewPort.verticalScrollBar().value()
        bottom = self.viewPort.verticalScrollBar().maximum() - 10
        if position > bottom:
            self.autoscroll = True
        self.actionAutoScroll.setChecked(self.autoscroll)
    
    def set_night_mode(self, nightmode=False):
        self.nightmode = nightmode
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
            self.setStyleSheet("background-color: rgb(162, 0, 0); color: rgb(200, 200, 200);" + "font: {}pt \"{}\";".format(font_size, font))
            self.menubar.setStyleSheet("background-color: rgb(162, 0, 0); color: rgb(200, 200, 200);" + "font: {}pt \"{}\";".format(font_size, font))
            self.toolBar.setStyleSheet("background-color: rgb(162, 0, 0); color: rgb(200, 200, 200);" + "font: {}pt \"{}\";".format(font_size, font))
        else:
            self.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);" + "font: {}pt \"{}\";".format(font_size, font))
            self.menubar.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);" + "font: {}pt \"{}\";".format(font_size, font))
            self.toolBar.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);" + "font: {}pt \"{}\";".format(font_size, font))
    
    def handle_disconnect_resume(self):
        """
        Disconnect, Reconnect button
        """
        if (self.serialClass != None):
            if self.serialClass.serial_running:
                # disconnect the serial so it is open to other processes
                self.serialClass.shutdown_serial()
                # Stop timer
                self.serialClass.uart_timer.stop()
                self.actionSuspend_Comm_Port.setText(
                    QtCore.QCoreApplication.translate("MainWindow", self.serialClass.comport + " Suspended"))
                self.actionSuspend_Comm_Port.setToolTip(
                    QtCore.QCoreApplication.translate("MainWindow", "Resume Comm Port"))
            else:
                self.serialClass.start_serial(self.serialClass.comport, self.serialClass.baudrate)
                self.serialClass.uart_timer.start()
                self.actionSuspend_Comm_Port.setText(
                    QtCore.QCoreApplication.translate("MainWindow", self.serialClass.comport + " Resumed"))
                self.actionSuspend_Comm_Port.setToolTip(
                    QtCore.QCoreApplication.translate("MainWindow", "Suspend Comm Port"))

    def onEditHistory(self):
        self.list_of_window = list()
        editHistory = EditHistory(self)
        self.list_of_window.append(editHistory)
        editHistory.show()


class App(object):
    def __init__(self):
        super().__init__()
        self.mainWindow = MainForm()
        try:
            self.mainWindow.show()
        except Exception as e:
            print(e)
