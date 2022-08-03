import os
import logging
import threading

from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication
from xmodem import XMODEM1k

from download_window import Ui_DownloadDialog
import config_utils
from xmodemclient import XmodemClient


class DownloadForm(QWidget, Ui_DownloadDialog):
    def __init__(self, serialhandler=None, mainwindow=None):
        super().__init__()
        self.setupUi(self)
        logging.basicConfig(level=logging.DEBUG)
        self.mainwindow = mainwindow
        self.serialhandle = serialhandler
        self.downloaddirectory = ""
        self.properties = dict()
        self.filename = None
        self.filesize = None
        self.xmodem = None
        self.log = logging.getLogger('DownloadForm')

        self.btnBrowse.clicked.connect(self.onBrowse)
        self.btnDownload.clicked.connect(self.onDownload)
        self.btnExit.clicked.connect(self.close)

        self.lblProgress.setText("")
        
        if self.serialhandle is not None:
            self.xmodem = XMODEM1k(getc=self.serialhandle.getc, putc=self.serialhandle.putc, pad=b'\xff')

        try:
            config_file = config_utils.read_config()
        except Exception as e:
            print(e)
            config_file = False

        if config_file:
            self.properties = config_file
            if 'downloaddirectory' in self.properties and self.properties['downloaddirectory']:
                self.downloaddirectory = self.properties['downloaddirectory']
                self.editSaveFolder.setText(self.downloaddirectory)
                self.btnDownload.setDisabled(False)

    def onBrowse(self):
        title = str("Select Directory")
        result = QFileDialog.getExistingDirectory(self, title, self.downloaddirectory)
        if result is not None:
            self.downloaddirectory = result
            self.editSaveFolder.setText(self.downloaddirectory)
            self.btnDownload.setDisabled(False)           # enable button
            try:
                if self.properties.update({"downloaddirectory":self.downloaddirectory}):
                    config_utils.save_confg(self.properties)
            except Exception as e:
                pass

    def onDownload(self):
        self.lblProgress.setText("")
        msg = QMessageBox()
        if self.editFilename.text() != "" and self.editSaveFolder.text() != "":
            downloadcmd = "At+XFXMODEMS=\"{}\"".format(self.editFilename.text())
            if self.editSaveAs.text() != "":
                self.filename = self.editSaveFolder.text() + "/" + self.editSaveAs.text()
            else:
                self.filename = self.editSaveFolder.text() + "/" + self.editFilename.text()

            self.ready = True
            if os.path.exists(self.filename):
                msg.setWindowTitle("File Exists")
                msg.setIcon(QMessageBox.Critical)
                msg.setText("File exists")
                result = msg.question(self, '', "Is it OK to overwrite file?", msg.Yes | msg.No)
                if result == msg.No:
                    self.ready = False

            if self.ready:
                msg.setStandardButtons(QMessageBox.Ok)
                success = self.doXmodem(downloadcmd)
                if success is not None:
                    if success:
                        string_to_show = "Received {} bytes\nFile {} saved as\n{}".format(self.filesize, self.editFilename.text(), self.filename)
                        msg.setWindowTitle("Success")
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Success")
                        msg.setDetailedText("Download Successful:\n{}".format(string_to_show))
                        msg.exec()
                    else:
                        msg.setWindowTitle("Error")
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error")
                        msg.setInformativeText('Download failed')
                        msg.exec()
        else:
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('No filename selected')
            msg.exec()

    def updateProgress(self, total_packets, success_count, error_count):
        message = "Blk: {}".format(success_count)
        self.lblProgress.setText(message)
        QApplication.processEvents()
        self.log.debug(message)

    def doXmodem(self, command):
        """
        Send directly to serial
        """
        if self.serialhandle.isReady():
            try:
                response = ""
                self.serialhandle.putc(str.encode(command + "\r\n"))
                while response != "OK" and response != "ERROR":
                    response = self.serialhandle.uart_rx()
                    if response is not None:
                        if "OK" in response:
                            response = "OK"
                        if "ERROR" in response:
                            response = "ERROR"

                if response == 'OK':
                    try:
                        dlThread = XmodemClient(self.serialhandle, self.filename, self.updateProgress, XmodemClient.DOWNLOAD)
                        dlThread.start()
                        dlThread.join()
#                        stream = open(self.filename, 'wb')
#                        self.filesize = self.xmodem.recv(stream, 1, 16, 60, 1, 0, self.updateProgress)
                    except Exception as e:
                        self.lblStatus.setText(str(e))
                        
                    while response != "XMODEMS SUCCESS" and response != "XMODEMS OK" and response != "XMODEMS FAILED":
                        response = self.serialhandle.uart_rx()
                        if response is not None:
                            if response.find('XMODEMS SUCCESS') != -1:
                                response = 'XMODEMS SUCCESS'
                                break
                            if response.find('XMODEMS OK') != -1:
                                response = 'XMODEMS OK'
                                break
                            if response.find('XMODEMS FAILED') != -1:
                                response = 'XMODEMS FAILED'
                                break
                    
                    if response == 'XMODEMS SUCCESS' or response == 'XMODEMS OK':
                        return True
                    else:
                        return False
                else:
                    return False
            except IOError as e:
                return False
        else:
            return None

    def xmodemThread(self):
        try:
            stream = open(self.filename, 'wb')
            self.filesize = self.xmodem.recv(stream, 1, 16, 60, 1, 0, self.updateProgress)
        finally:
            stream.close()

