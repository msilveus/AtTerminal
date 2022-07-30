# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\download_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        DownloadDialog.setObjectName("DownloadDialog")
        DownloadDialog.resize(452, 225)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DownloadDialog.setWindowIcon(icon)
        DownloadDialog.setStyleSheet("font: 12pt \"Cascadia Mono\";")
        self.gridLayout = QtWidgets.QGridLayout(DownloadDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(DownloadDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.editFilename = QtWidgets.QLineEdit(DownloadDialog)
        self.editFilename.setObjectName("editFilename")
        self.verticalLayout_3.addWidget(self.editFilename)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(DownloadDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.editSaveAs = QtWidgets.QLineEdit(DownloadDialog)
        self.editSaveAs.setObjectName("editSaveAs")
        self.verticalLayout_2.addWidget(self.editSaveAs)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblProgress = QtWidgets.QLabel(DownloadDialog)
        self.lblProgress.setObjectName("lblProgress")
        self.horizontalLayout_2.addWidget(self.lblProgress)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnDownload = QtWidgets.QPushButton(DownloadDialog)
        self.btnDownload.setEnabled(False)
        self.btnDownload.setObjectName("btnDownload")
        self.horizontalLayout_3.addWidget(self.btnDownload)
        self.btnExit = QtWidgets.QPushButton(DownloadDialog)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout_3.addWidget(self.btnExit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(DownloadDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editSaveFolder = QtWidgets.QLineEdit(DownloadDialog)
        self.editSaveFolder.setObjectName("editSaveFolder")
        self.horizontalLayout.addWidget(self.editSaveFolder)
        self.btnBrowse = QtWidgets.QPushButton(DownloadDialog)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.lblStatus = QtWidgets.QLabel(DownloadDialog)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 3, 0, 1, 1)

        self.retranslateUi(DownloadDialog)
        QtCore.QMetaObject.connectSlotsByName(DownloadDialog)

    def retranslateUi(self, DownloadDialog):
        _translate = QtCore.QCoreApplication.translate
        DownloadDialog.setWindowTitle(_translate("DownloadDialog", "Download"))
        self.label_2.setText(_translate("DownloadDialog", "File to Download "))
        self.label_3.setText(_translate("DownloadDialog", "Save As"))
        self.editSaveAs.setToolTip(_translate("DownloadDialog", "Leave Blank for same"))
        self.editSaveAs.setPlaceholderText(_translate("DownloadDialog", "Same name if blank"))
        self.lblProgress.setText(_translate("DownloadDialog", "Blk:"))
        self.btnDownload.setText(_translate("DownloadDialog", "Download"))
        self.btnExit.setText(_translate("DownloadDialog", "Exit"))
        self.label.setText(_translate("DownloadDialog", "Save Location"))
        self.btnBrowse.setText(_translate("DownloadDialog", "Browse"))
import images_rc
