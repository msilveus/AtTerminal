import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QFileDialog
from xmodem import XMODEM1k

import config_utils
from upload_window import Ui_uploadForm


class UploadForm(QWidget, Ui_uploadForm):
    def __init__(self, serialhandler=None, mainwindow=None):
        super().__init__()
        self.setupUi(self)

        self.btnBrowse.clicked.connect(self.onBrowse)
        self.btnCancel.clicked.connect(self.close)
        self.btnUpload.clicked.connect(self.onUpload)
        self.btnUpload.setDisabled(True)

        self.serialhandle = serialhandler
        self.mainwindow = mainwindow
        self.xmodem = None
        self.filename = None
        self.filesize = 0
        self.uploadDirectory = ''

        self.one_sec_timer = QTimer()
        self.one_sec_timer.setInterval(1000)
        self.one_sec_timer.timeout.connect(self.one_sec_handler)

        if self.serialhandle is not None:
            self.xmodem = XMODEM1k(getc=self.serialhandle.getc, putc=self.serialhandle.putc, pad=b'\xff')

        try:
            config_file = config_utils.read_config()
        except Exception as e:
            print(e)
            config_file = False
    
        if config_file:
            self.properties = config_file
            if 'uploaddirectory' in self.properties and self.properties['uploaddirectory']:
                self.uploadDirectory = self.properties['uploaddirectory']

    def onBrowse(self):
        title = str("Select a file to upload")
        filter = str(
                'all_supported_files (*.azip *.bin *.cfg *.txt);; '
                'azip (*.azip);;'
                'bin (*.bin);; '
                'cfg (*.cfg);;'
                'txt (*.txt);;'
                'all_files (*)')
        result = QFileDialog.getOpenFileName(self, title, self.uploadDirectory,filter)
        if result is not None:
            self.filename = result[0]
            self.editFilename.setText(self.filename) # extract filename from tuple
            self.btnUpload.setDisabled(False)           # enable button
            self.uploadDirectory = os.path.dirname(self.filename)
            self.properties.update({"uploaddirectory":self.uploadDirectory})
            config_utils.save_confg(self.properties)

    def onUpload(self):
        uploadcmd = None
        filetype = None
        fileid = None
        shouldreset = False

        filesize = os.stat(self.filename).st_size
        boxElements = self.uploadMode.children()
    
        radioButtons = [elem for elem in boxElements if isinstance(elem, QtWidgets.QRadioButton)]
        for rb in radioButtons:
            if rb.isChecked():
                if rb == self.rbtnApplication:
                    fileid = "custom.rom"
                    uploadcmd = "At+XFXMODEMR=\"{}\",{}".format(fileid, filesize)
                    filetype = 1
                    shouldreset = True
                elif rb == self.rbtnMCU:
                    fileid = "mcu.bin"
                    uploadcmd = "At+XFXMODEMR=\"{}\",{}".format(fileid, filesize)
                    filetype = 2
                    shouldreset = False
                elif rb == self.rbtnDefaultCfg:
                    fileid = "default.cfg"
                    uploadcmd = "At+XFXMODEMR=\"{}\",{}".format(fileid, filesize)
                    filetype = 3
                    shouldreset = True
                elif rb == self.rbtnUserCfg:
                    fileid = "user.cfg"
                    uploadcmd = "At+XFXMODEMR=\"{}\",{}".format(fileid, filesize)
                    filetype = 4
                    shouldreset = True
                elif rb == self.rbtnCS:
                    fileid = "cs.update"
                    uploadcmd = "At+XFXMODEMR=\"{}\",{}".format(fileid, filesize)
                    filetype = 5
                    shouldreset = False
                elif rb == self.rbtnCPFW:
                    fileid = "CPupdate.bin"
                    uploadcmd = "At+XFXMODEMR=\"{}\",{}".format(fileid, filesize)
                    filetype = 6
                    shouldreset = False
                elif rb == self.rbtnCPFW:
                    fileid = "nalamux.bin"
                    uploadcmd = "At+XFXMODEMR=\"{}\",{}".format(fileid, filesize)
                    filetype = 9
                    shouldreset = False

        if uploadcmd is not None:
            self.serialhandle.setUploadMode(True)  # disable normal processing
            if self.doXmodem(uploadcmd):
                self.fupdate(filetype, fileid)
                if shouldreset:
                    self.doReset(2) # soft reset
            self.serialhandle.setUploadMode(False) # re-enable normal processing
            self.close()

    def doXmodem(self, command):
        """
        Send directly to serial
        """
        if self.serialhandle.isReady():
            try:
                self.lblStatus.setText("Sending {}".format(command))
                response = ""
                self.serialhandle.putc(str.encode(command + "\r\n"))
                while response != "OK" and response != "ERROR":
                    response = self.serialhandle.uart_rx()

                if response == 'OK':
                    try:
                        stream = open(self.filename, 'rb')
                        self.filesize = os.stat(self.filename).st_size
                        self.xmodem.send(stream, 128, 60, False, self.updateProgressBar)
                        
                    finally:
                        stream.close()
                    while response != "XMODEMR SUCCESS" and response != "XMODEMR OK" and response != "XMODEMR FAILED":
                        response = self.serialhandle.uart_rx()

                    if response == 'XMODEMR SUCCESS' or response == 'XMODEMR OK':
                        return True
                    else:
                        return False
                else:
                    return False
            except IOError as e:
                return False
        else:
            return None

    def updateProgressBar(self, total_packets, success_count, error_count):
        total_blks = self.filesize / 1024
        if self.filesize % 1024:
            total_blks = total_blks + 1
        percent = (success_count / int(total_blks)) * 100
        self.progressBar.setValue(int(percent))

    def fupdate(self, type=None, fileid=None):
        if type is not None and fileid is not None:
            fupdatecmd = "AT+XFUPDATE=\"{}\",{}".format(str(fileid), str(type))

            self.lblStatus.setText("Sending {}".format(fupdatecmd))
            response = ""
            self.serialhandle.putc(str.encode(fupdatecmd + "\r\n"))
    
            while response != "OK" and response != "ERROR":
                response = self.serialhandle.uart_rx()

    def doReset(self, type=None):
        resetcmd = "AT+XRST={}".format(type)

        self.lblStatus.setText("Sending {}".format(resetcmd))
        response = ""
        self.serialhandle.putc(str.encode(resetcmd + "\r\n"))

        while response != "OK" and response != "ERROR":
            response = self.serialhandle.uart_rx()

    def one_sec_handler(self):
        pass

