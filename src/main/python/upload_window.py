# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\upload_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uploadForm(object):
    def setupUi(self, uploadForm):
        uploadForm.setObjectName("uploadForm")
        uploadForm.setWindowModality(QtCore.Qt.NonModal)
        uploadForm.resize(500, 392)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        uploadForm.setWindowIcon(icon)
        uploadForm.setStyleSheet("font: 12pt \"Cascadia Mono\";")
        self.gridLayout = QtWidgets.QGridLayout(uploadForm)
        self.gridLayout.setObjectName("gridLayout")
        self.uploadMode = QtWidgets.QGroupBox(uploadForm)
        self.uploadMode.setObjectName("uploadMode")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uploadMode)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbtnApplication = QtWidgets.QRadioButton(self.uploadMode)
        self.rbtnApplication.setChecked(True)
        self.rbtnApplication.setObjectName("rbtnApplication")
        self.verticalLayout.addWidget(self.rbtnApplication)
        self.rbtnMCU = QtWidgets.QRadioButton(self.uploadMode)
        self.rbtnMCU.setObjectName("rbtnMCU")
        self.verticalLayout.addWidget(self.rbtnMCU)
        self.rbtnDefaultCfg = QtWidgets.QRadioButton(self.uploadMode)
        self.rbtnDefaultCfg.setObjectName("rbtnDefaultCfg")
        self.verticalLayout.addWidget(self.rbtnDefaultCfg)
        self.rbtnUserCfg = QtWidgets.QRadioButton(self.uploadMode)
        self.rbtnUserCfg.setObjectName("rbtnUserCfg")
        self.verticalLayout.addWidget(self.rbtnUserCfg)
        self.rbtnCS = QtWidgets.QRadioButton(self.uploadMode)
        self.rbtnCS.setObjectName("rbtnCS")
        self.verticalLayout.addWidget(self.rbtnCS)
        self.rbtnCPFW = QtWidgets.QRadioButton(self.uploadMode)
        self.rbtnCPFW.setObjectName("rbtnCPFW")
        self.verticalLayout.addWidget(self.rbtnCPFW)
        self.rbtnNalaMux = QtWidgets.QRadioButton(self.uploadMode)
        self.rbtnNalaMux.setObjectName("rbtnNalaMux")
        self.verticalLayout.addWidget(self.rbtnNalaMux)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.uploadMode, 0, 0, 2, 2)
        self.lblStatus = QtWidgets.QLabel(uploadForm)
        self.lblStatus.setText("")
        self.lblStatus.setObjectName("lblStatus")
        self.gridLayout.addWidget(self.lblStatus, 3, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.optionsBox = QtWidgets.QGroupBox(uploadForm)
        self.optionsBox.setObjectName("optionsBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.optionsBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rbtnFactory = QtWidgets.QRadioButton(self.optionsBox)
        self.rbtnFactory.setChecked(True)
        self.rbtnFactory.setObjectName("rbtnFactory")
        self.verticalLayout_5.addWidget(self.rbtnFactory)
        self.rbtnReset = QtWidgets.QRadioButton(self.optionsBox)
        self.rbtnReset.setObjectName("rbtnReset")
        self.verticalLayout_5.addWidget(self.rbtnReset)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addWidget(self.optionsBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 2, 2, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.progressBar = QtWidgets.QProgressBar(uploadForm)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.editFilename = QtWidgets.QLineEdit(uploadForm)
        self.editFilename.setObjectName("editFilename")
        self.horizontalLayout.addWidget(self.editFilename)
        self.btnBrowse = QtWidgets.QPushButton(uploadForm)
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnUpload = QtWidgets.QPushButton(uploadForm)
        self.btnUpload.setObjectName("btnUpload")
        self.verticalLayout_2.addWidget(self.btnUpload)
        self.btnCancel = QtWidgets.QPushButton(uploadForm)
        self.btnCancel.setObjectName("btnCancel")
        self.verticalLayout_2.addWidget(self.btnCancel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 5)

        self.retranslateUi(uploadForm)
        QtCore.QMetaObject.connectSlotsByName(uploadForm)

    def retranslateUi(self, uploadForm):
        _translate = QtCore.QCoreApplication.translate
        uploadForm.setWindowTitle(_translate("uploadForm", "Upload"))
        self.uploadMode.setTitle(_translate("uploadForm", "Upload Mode"))
        self.rbtnApplication.setText(_translate("uploadForm", "Application"))
        self.rbtnMCU.setText(_translate("uploadForm", "MCU"))
        self.rbtnDefaultCfg.setText(_translate("uploadForm", "Default Config"))
        self.rbtnUserCfg.setText(_translate("uploadForm", "User Config"))
        self.rbtnCS.setText(_translate("uploadForm", "Cargo Sensor"))
        self.rbtnCPFW.setText(_translate("uploadForm", "CP FW"))
        self.rbtnNalaMux.setText(_translate("uploadForm", "Nala Mux"))
        self.optionsBox.setTitle(_translate("uploadForm", "Options"))
        self.rbtnFactory.setText(_translate("uploadForm", "Factory"))
        self.rbtnReset.setText(_translate("uploadForm", "Soft Reset"))
        self.btnBrowse.setText(_translate("uploadForm", "Browse"))
        self.btnUpload.setText(_translate("uploadForm", "Upload"))
        self.btnCancel.setText(_translate("uploadForm", "Cancel"))
import images_rc
