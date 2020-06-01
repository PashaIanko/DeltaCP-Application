from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.aaa = QtWidgets.QTabWidget(self.centralwidget)
        self.aaa.setGeometry(QtCore.QRect(20, 60, 731, 411))
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
        self.TestpushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.TestpushButton.setGeometry(QtCore.QRect(10, 170, 93, 28))
        self.TestpushButton.setObjectName("TestpushButton")
        self.FreqMintextEdit = QtWidgets.QTextEdit(self.OutputFrequencySettingTab)
        self.FreqMintextEdit.setEnabled(False)
        self.FreqMintextEdit.setGeometry(QtCore.QRect(390, 40, 41, 41))
        self.FreqMintextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FreqMintextEdit.setObjectName("FreqMintextEdit")
        self.FreqMaxtextEdit = QtWidgets.QTextEdit(self.OutputFrequencySettingTab)
        self.FreqMaxtextEdit.setEnabled(False)
        self.FreqMaxtextEdit.setGeometry(QtCore.QRect(660, 40, 41, 41))
        self.FreqMaxtextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FreqMaxtextEdit.setObjectName("FreqMaxtextEdit")
        self.SetFreqpushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.SetFreqpushButton.setGeometry(QtCore.QRect(210, 120, 93, 28))
        self.SetFreqpushButton.setObjectName("SetFreqpushButton")
        self.RunpushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.RunpushButton.setGeometry(QtCore.QRect(10, 120, 93, 28))
        self.RunpushButton.setObjectName("RunpushButton")
        self.StoppushButton = QtWidgets.QPushButton(self.OutputFrequencySettingTab)
        self.StoppushButton.setGeometry(QtCore.QRect(110, 120, 93, 28))
        self.StoppushButton.setObjectName("StoppushButton")
        self.layoutWidget2 = QtWidgets.QWidget(self.OutputFrequencySettingTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 40, 267, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.FrequencySetlineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.FrequencySetlineEdit.setObjectName("FrequencySetlineEdit")
        self.horizontalLayout_3.addWidget(self.FrequencySetlineEdit)
        self.layoutWidget.raise_()
        self.HztextEdit.raise_()
        self.TestpushButton.raise_()
        self.FreqMintextEdit.raise_()
        self.FrequencySetSlider.raise_()
        self.FreqMaxtextEdit.raise_()
        self.SetFreqpushButton.raise_()
        self.RunpushButton.raise_()
        self.StoppushButton.raise_()
        self.aaa.addTab(self.OutputFrequencySettingTab, "")
        self.FrequencySignalSetting = QtWidgets.QWidget()
        self.FrequencySignalSetting.setObjectName("FrequencySignalSetting")
        self.SignalTypecomboBox = QtWidgets.QComboBox(self.FrequencySignalSetting)
        self.SignalTypecomboBox.setGeometry(QtCore.QRect(150, 50, 73, 22))
        self.SignalTypecomboBox.setObjectName("SignalTypecomboBox")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.setItemText(0, "")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.FrequencySignalSetting)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 96, 22))
        self.label_4.setObjectName("label_4")
        self.aaa.addTab(self.FrequencySignalSetting, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.aaa.setCurrentIndex(0)
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
        self.TestpushButton.setText(_translate("MainWindow", "TestButton"))
        self.FreqMintextEdit.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.FreqMaxtextEdit.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">100</span></p></body></html>"))
        self.SetFreqpushButton.setText(_translate("MainWindow", "Set frequency"))
        self.RunpushButton.setText(_translate("MainWindow", "Run"))
        self.StoppushButton.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "Output frequency:"))
        self.FrequencySetlineEdit.setText(_translate("MainWindow", "0"))
        self.aaa.setTabText(self.aaa.indexOf(self.OutputFrequencySettingTab),
                            _translate("MainWindow", "Output Frequency Setting"))
        self.SignalTypecomboBox.setItemText(1, _translate("MainWindow", "sin"))
        self.SignalTypecomboBox.setItemText(2, _translate("MainWindow", "meander"))
        self.SignalTypecomboBox.setItemText(3, _translate("MainWindow", "saw"))
        self.label_4.setText(_translate("MainWindow", "Signal type:"))
        self.aaa.setTabText(self.aaa.indexOf(self.FrequencySignalSetting),
                            _translate("MainWindow", "Frequency Signal Setting"))
        self.menuConnection_Parameters.setTitle(_translate("MainWindow", "Connection Parameters"))
        self.menuOutput_Frequency_Settings.setTitle(_translate("MainWindow", "Output Frequency Settings"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))


