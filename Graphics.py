from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.aaa = QtWidgets.QTabWidget(self.centralwidget)
        self.aaa.setGeometry(QtCore.QRect(20, 70, 1322, 411))
        self.aaa.setObjectName("aaa")
        self.ConnectionParametersTab = QtWidgets.QWidget()
        self.ConnectionParametersTab.setObjectName("ConnectionParametersTab")
        self.layoutWidget = QtWidgets.QWidget(self.ConnectionParametersTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 250, 195, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AutoConnectpushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.AutoConnectpushButton.setObjectName("AutoConnectpushButton")
        self.horizontalLayout.addWidget(self.AutoConnectpushButton)
        self.ConnectpushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.ConnectpushButton.setObjectName("ConnectpushButton")
        self.horizontalLayout.addWidget(self.ConnectpushButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.ConnectionParametersTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 235, 227))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.BaudRateLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.BaudRateLabel.setObjectName("BaudRateLabel")
        self.gridLayout.addWidget(self.BaudRateLabel, 6, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 2)
        self.ComPortNumberlabel = QtWidgets.QLabel(self.layoutWidget1)
        self.ComPortNumberlabel.setObjectName("ComPortNumberlabel")
        self.gridLayout.addWidget(self.ComPortNumberlabel, 5, 0, 1, 3)
        self.COMPortcomboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.COMPortcomboBox.setObjectName("COMPortcomboBox")
        self.COMPortcomboBox.addItem("")
        self.COMPortcomboBox.setItemText(0, "")
        self.COMPortcomboBox.addItem("")
        self.COMPortcomboBox.addItem("")
        self.COMPortcomboBox.addItem("")
        self.COMPortcomboBox.addItem("")
        self.COMPortcomboBox.addItem("")
        self.COMPortcomboBox.addItem("")
        self.COMPortcomboBox.addItem("")
        self.gridLayout.addWidget(self.COMPortcomboBox, 5, 3, 1, 2)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.StopBitscomboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.StopBitscomboBox.setObjectName("StopBitscomboBox")
        self.StopBitscomboBox.addItem("")
        self.StopBitscomboBox.setItemText(0, "")
        self.StopBitscomboBox.addItem("")
        self.StopBitscomboBox.addItem("")
        self.gridLayout.addWidget(self.StopBitscomboBox, 4, 3, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.BaudRatecomboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.BaudRatecomboBox.setObjectName("BaudRatecomboBox")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.setItemText(0, "")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.addItem("")
        self.gridLayout.addWidget(self.BaudRatecomboBox, 6, 3, 1, 2)
        self.ByteSizecomboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.ByteSizecomboBox.setObjectName("ByteSizecomboBox")
        self.ByteSizecomboBox.addItem("")
        self.ByteSizecomboBox.setItemText(0, "")
        self.ByteSizecomboBox.addItem("")
        self.ByteSizecomboBox.addItem("")
        self.gridLayout.addWidget(self.ByteSizecomboBox, 1, 3, 1, 2)
        self.ParitycomboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.ParitycomboBox.setObjectName("ParitycomboBox")
        self.ParitycomboBox.addItem("")
        self.ParitycomboBox.setItemText(0, "")
        self.ParitycomboBox.addItem("")
        self.ParitycomboBox.addItem("")
        self.ParitycomboBox.addItem("")
        self.gridLayout.addWidget(self.ParitycomboBox, 3, 3, 1, 2)
        self.ProtocolcomboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.ProtocolcomboBox.setObjectName("ProtocolcomboBox")
        self.ProtocolcomboBox.addItem("")
        self.ProtocolcomboBox.setItemText(0, "")
        self.ProtocolcomboBox.addItem("")
        self.ProtocolcomboBox.addItem("")
        self.gridLayout.addWidget(self.ProtocolcomboBox, 0, 3, 1, 2)
        self.aaa.addTab(self.ConnectionParametersTab, "")
        self.OutputFrequencySettingTab = QtWidgets.QWidget()
        self.OutputFrequencySettingTab.setObjectName("OutputFrequencySettingTab")
        self.FrequencySetSlider = QtWidgets.QSlider(self.OutputFrequencySettingTab)
        self.FrequencySetSlider.setGeometry(QtCore.QRect(420, 50, 231, 22))
        self.FrequencySetSlider.setMaximum(50)
        self.FrequencySetSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FrequencySetSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.FrequencySetSlider.setObjectName("FrequencySetSlider")
        self.HztextEdit = QtWidgets.QTextEdit(self.OutputFrequencySettingTab)
        self.HztextEdit.setEnabled(False)
        self.HztextEdit.setGeometry(QtCore.QRect(280, 50, 51, 21))
        self.HztextEdit.setAutoFillBackground(False)
        self.HztextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HztextEdit.setObjectName("HztextEdit")
        self.SetFrequencypushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.SetFrequencypushButton.setGeometry(QtCore.QRect(20, 110, 93, 28))
        self.SetFrequencypushButton.setObjectName("SetFrequencypushButton")
        self.StopFrequencypushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.StopFrequencypushButton.setGeometry(QtCore.QRect(220, 110, 93, 28))
        self.StopFrequencypushButton.setObjectName("StopFrequencypushButton")
        self.layoutWidget2 = QtWidgets.QWidget(self.OutputFrequencySettingTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 40, 267, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.OutputFrequencylineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.OutputFrequencylineEdit.setObjectName("OutputFrequencylineEdit")
        self.horizontalLayout_3.addWidget(self.OutputFrequencylineEdit)
        self.FrequencyMinlineEdit = QtWidgets.QLineEdit(self.OutputFrequencySettingTab)
        self.FrequencyMinlineEdit.setGeometry(QtCore.QRect(360, 50, 51, 22))
        self.FrequencyMinlineEdit.setObjectName("FrequencyMinlineEdit")
        self.FrequencyMaxlineEdit = QtWidgets.QLineEdit(self.OutputFrequencySettingTab)
        self.FrequencyMaxlineEdit.setGeometry(QtCore.QRect(660, 50, 51, 22))
        self.FrequencyMaxlineEdit.setObjectName("FrequencyMaxlineEdit")
        self.StartFrequencypushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.StartFrequencypushButton.setGeometry(QtCore.QRect(120, 110, 93, 28))
        self.StartFrequencypushButton.setObjectName("StartFrequencypushButton")
        self.RequestCurrentFrequencypushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.RequestCurrentFrequencypushButton.setGeometry(QtCore.QRect(20, 150, 101, 51))
        self.RequestCurrentFrequencypushButton.setObjectName("RequestCurrentFrequencypushButton")
        self.RequestSetFrequencypushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.RequestSetFrequencypushButton.setGeometry(QtCore.QRect(120, 150, 93, 51))
        self.RequestSetFrequencypushButton.setObjectName("RequestSetFrequencypushButton")
        self.layoutWidget.raise_()
        self.HztextEdit.raise_()
        self.FrequencySetSlider.raise_()
        self.SetFrequencypushButton.raise_()
        self.StopFrequencypushButton.raise_()
        self.FrequencyMinlineEdit.raise_()
        self.FrequencyMaxlineEdit.raise_()
        self.StartFrequencypushButton.raise_()
        self.RequestCurrentFrequencypushButton.raise_()
        self.RequestSetFrequencypushButton.raise_()
        self.aaa.addTab(self.OutputFrequencySettingTab, "")
        self.FrequencySignalSetting = QtWidgets.QWidget()
        self.FrequencySignalSetting.setObjectName("FrequencySignalSetting")
        self.SignalTypecomboBox = QtWidgets.QComboBox(self.FrequencySignalSetting)
        self.SignalTypecomboBox.setGeometry(QtCore.QRect(150, 50, 151, 22))
        self.SignalTypecomboBox.setObjectName("SignalTypecomboBox")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.setItemText(0, "")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.FrequencySignalSetting)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 96, 22))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.FrequencySignalSetting)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 100, 351, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.AccelerationTimelabel_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.AccelerationTimelabel_2.setObjectName("AccelerationTimelabel_2")
        self.horizontalLayout_5.addWidget(self.AccelerationTimelabel_2)
        self.AccDec1radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.AccDec1radioButton.setChecked(True)
        self.AccDec1radioButton.setObjectName("AccDec1radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec1radioButton)
        self.AccDec2radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.AccDec2radioButton.setObjectName("AccDec2radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec2radioButton)
        self.AccDec3radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.AccDec3radioButton.setObjectName("AccDec3radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec3radioButton)
        self.AccDec4radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.AccDec4radioButton.setObjectName("AccDec4radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec4radioButton)
        self.aaa.addTab(self.FrequencySignalSetting, "")
        self.SignalSendingTab = QtWidgets.QWidget()
        self.SignalSendingTab.setObjectName("SignalSendingTab")
        self.pushButtonStartSignalSending = QtWidgets.QPushButton(self.SignalSendingTab)
        self.pushButtonStartSignalSending.setGeometry(QtCore.QRect(40, 60, 131, 41))
        self.pushButtonStartSignalSending.setObjectName("pushButtonStartSignalSending")
        self.PauseSendingradioButton = QtWidgets.QRadioButton(self.SignalSendingTab)
        self.PauseSendingradioButton.setGeometry(QtCore.QRect(40, 130, 95, 20))
        self.PauseSendingradioButton.setObjectName("PauseSendingradioButton")
        self.ResumeSendingradioButton = QtWidgets.QRadioButton(self.SignalSendingTab)
        self.ResumeSendingradioButton.setGeometry(QtCore.QRect(130, 130, 95, 20))
        self.ResumeSendingradioButton.setChecked(True)
        self.ResumeSendingradioButton.setAutoExclusive(True)
        self.ResumeSendingradioButton.setObjectName("ResumeSendingradioButton")
        self.pushButtonStopSignalSending = QtWidgets.QPushButton(self.SignalSendingTab)
        self.pushButtonStopSignalSending.setGeometry(QtCore.QRect(40, 170, 131, 41))
        self.pushButtonStopSignalSending.setObjectName("pushButtonStopSignalSending")
        self.EndlessSendingcheckBox = QtWidgets.QCheckBox(self.SignalSendingTab)
        self.EndlessSendingcheckBox.setGeometry(QtCore.QRect(200, 70, 191, 20))
        self.EndlessSendingcheckBox.setObjectName("EndlessSendingcheckBox")
        self.aaa.addTab(self.SignalSendingTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName("menubar")
        self.menuConnection_Parameters = QtWidgets.QMenu(self.menubar)
        self.menuConnection_Parameters.setObjectName("menuConnection_Parameters")
        self.menuOutput_Frequency_Settings = QtWidgets.QMenu(self.menubar)
        self.menuOutput_Frequency_Settings.setObjectName("menuOutput_Frequency_Settings")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuConnection_Parameters.addSeparator()
        self.menubar.addAction(self.menuConnection_Parameters.menuAction())
        self.menubar.addAction(self.menuOutput_Frequency_Settings.menuAction())
        self.menubar.addAction(self.menuNew.menuAction())

        self.retranslateUi(MainWindow)
        self.aaa.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.AutoConnectpushButton.setText(_translate("MainWindow", "Auto-Connect"))
        self.ConnectpushButton.setText(_translate("MainWindow", "Connect"))
        self.BaudRateLabel.setText(_translate("MainWindow", "Baud Rate: "))
        self.label_6.setText(_translate("MainWindow", "Stop Bits:"))
        self.ComPortNumberlabel.setText(_translate("MainWindow", "COM Port Number:"))
        self.COMPortcomboBox.setItemText(1, _translate("MainWindow", "COM1"))
        self.COMPortcomboBox.setItemText(2, _translate("MainWindow", "COM2"))
        self.COMPortcomboBox.setItemText(3, _translate("MainWindow", "COM3"))
        self.COMPortcomboBox.setItemText(4, _translate("MainWindow", "COM4"))
        self.COMPortcomboBox.setItemText(5, _translate("MainWindow", "COM5"))
        self.COMPortcomboBox.setItemText(6, _translate("MainWindow", "COM6"))
        self.COMPortcomboBox.setItemText(7, _translate("MainWindow", "COM7"))
        self.label.setText(_translate("MainWindow", "Protocol:"))
        self.label_2.setText(_translate("MainWindow", "Byte size"))
        self.StopBitscomboBox.setItemText(1, _translate("MainWindow", "1"))
        self.StopBitscomboBox.setItemText(2, _translate("MainWindow", "2"))
        self.label_5.setText(_translate("MainWindow", "Parity:"))
        self.BaudRatecomboBox.setItemText(1, _translate("MainWindow", "1200"))
        self.BaudRatecomboBox.setItemText(2, _translate("MainWindow", "2400"))
        self.BaudRatecomboBox.setItemText(3, _translate("MainWindow", "3600"))
        self.BaudRatecomboBox.setItemText(4, _translate("MainWindow", "9600"))
        self.ByteSizecomboBox.setItemText(1, _translate("MainWindow", "7"))
        self.ByteSizecomboBox.setItemText(2, _translate("MainWindow", "8"))
        self.ParitycomboBox.setItemText(1, _translate("MainWindow", "O"))
        self.ParitycomboBox.setItemText(2, _translate("MainWindow", "N"))
        self.ParitycomboBox.setItemText(3, _translate("MainWindow", "E"))
        self.ProtocolcomboBox.setItemText(1, _translate("MainWindow", "rtu"))
        self.ProtocolcomboBox.setItemText(2, _translate("MainWindow", "ascii"))
        self.aaa.setTabText(self.aaa.indexOf(self.ConnectionParametersTab),
                            _translate("MainWindow", "Connection Parameters"))
        self.HztextEdit.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Hz</span></p></body></html>"))
        self.SetFrequencypushButton.setText(_translate("MainWindow", "Set frequency"))
        self.StopFrequencypushButton.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "Output frequency:"))
        self.OutputFrequencylineEdit.setText(_translate("MainWindow", "0"))
        self.FrequencyMinlineEdit.setText(_translate("MainWindow", "0"))
        self.FrequencyMaxlineEdit.setText(_translate("MainWindow", "100"))
        self.StartFrequencypushButton.setText(_translate("MainWindow", "Start"))
        self.RequestCurrentFrequencypushButton.setText(_translate("MainWindow", "Request Current\n"
                                                                                "Frequency"))
        self.RequestSetFrequencypushButton.setText(_translate("MainWindow", "Request Set \n"
                                                                            "Frequency"))
        self.aaa.setTabText(self.aaa.indexOf(self.OutputFrequencySettingTab),
                            _translate("MainWindow", "Output Frequency Setting"))
        self.SignalTypecomboBox.setItemText(1, _translate("MainWindow", "sin"))
        self.SignalTypecomboBox.setItemText(2, _translate("MainWindow", "user signal"))
        self.SignalTypecomboBox.setItemText(3, _translate("MainWindow", "dynamic points density"))
        self.label_4.setText(_translate("MainWindow", "Signal type:"))
        self.AccelerationTimelabel_2.setText(_translate("MainWindow", "Acceleration\n"
                                                                      "Deceleration\n"
                                                                      " Regime:"))
        self.AccDec1radioButton.setText(_translate("MainWindow", "1"))
        self.AccDec2radioButton.setText(_translate("MainWindow", "2"))
        self.AccDec3radioButton.setText(_translate("MainWindow", "3"))
        self.AccDec4radioButton.setText(_translate("MainWindow", "4"))
        self.aaa.setTabText(self.aaa.indexOf(self.FrequencySignalSetting),
                            _translate("MainWindow", "Frequency Signal Setting"))
        self.pushButtonStartSignalSending.setText(_translate("MainWindow", "Start Signal Sending"))
        self.PauseSendingradioButton.setText(_translate("MainWindow", "Pause"))
        self.ResumeSendingradioButton.setText(_translate("MainWindow", "Resume"))
        self.pushButtonStopSignalSending.setText(_translate("MainWindow", "Stop Signal Sending"))
        self.EndlessSendingcheckBox.setText(_translate("MainWindow", "Send Pattern Continuously"))
        self.aaa.setTabText(self.aaa.indexOf(self.SignalSendingTab),
                            _translate("MainWindow", "Signal Sending to Delta PC"))
        self.menuConnection_Parameters.setTitle(_translate("MainWindow", "Connection Parameters"))
        self.menuOutput_Frequency_Settings.setTitle(_translate("MainWindow", "Output Frequency Settings"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))