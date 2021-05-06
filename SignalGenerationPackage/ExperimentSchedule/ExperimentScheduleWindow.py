from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExperimentScheduleWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 850)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(700, 80))
        self.frame_3.setMaximumSize(QtCore.QSize(1500, 90))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.ConfigFileNamelineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.ConfigFileNamelineEdit.setMinimumSize(QtCore.QSize(250, 0))
        self.ConfigFileNamelineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ConfigFileNamelineEdit.setFont(font)
        self.ConfigFileNamelineEdit.setObjectName("ConfigFileNamelineEdit")
        self.horizontalLayout.addWidget(self.ConfigFileNamelineEdit)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.AutoFillpushButton = QtWidgets.QPushButton(self.frame_8)
        self.AutoFillpushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.AutoFillpushButton.setObjectName("AutoFillpushButton")
        self.gridLayout_10.addWidget(self.AutoFillpushButton, 0, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame_8)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.LogFilenamelineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.LogFilenamelineEdit.setMinimumSize(QtCore.QSize(260, 0))
        self.LogFilenamelineEdit.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LogFilenamelineEdit.setFont(font)
        self.LogFilenamelineEdit.setObjectName("LogFilenamelineEdit")
        self.horizontalLayout.addWidget(self.LogFilenamelineEdit)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(300, 400))
        self.frame_7.setMaximumSize(QtCore.QSize(300, 600))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.formLayout = QtWidgets.QFormLayout(self.frame_7)
        self.formLayout.setObjectName("formLayout")
        self.frame = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 100))
        self.frame.setMaximumSize(QtCore.QSize(400, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(80, 20))
        self.lcdNumber.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_7)
        self.frame_4.setMinimumSize(QtCore.QSize(300, 400))
        self.frame_4.setMaximumSize(QtCore.QSize(400, 150))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButtonStartSignalSending = QtWidgets.QPushButton(self.frame_5)
        self.pushButtonStartSignalSending.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButtonStartSignalSending.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStartSignalSending.setObjectName("pushButtonStartSignalSending")
        self.gridLayout_6.addWidget(self.pushButtonStartSignalSending, 0, 0, 1, 2)
        self.PauseSendingradioButton = QtWidgets.QRadioButton(self.frame_5)
        self.PauseSendingradioButton.setObjectName("PauseSendingradioButton")
        self.gridLayout_6.addWidget(self.PauseSendingradioButton, 1, 0, 1, 1)
        self.ResumeSendingradioButton = QtWidgets.QRadioButton(self.frame_5)
        self.ResumeSendingradioButton.setChecked(True)
        self.ResumeSendingradioButton.setAutoExclusive(True)
        self.ResumeSendingradioButton.setObjectName("ResumeSendingradioButton")
        self.gridLayout_6.addWidget(self.ResumeSendingradioButton, 1, 1, 1, 1)
        self.pushButtonStopSignalSending = QtWidgets.QPushButton(self.frame_5)
        self.pushButtonStopSignalSending.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButtonStopSignalSending.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStopSignalSending.setObjectName("pushButtonStopSignalSending")
        self.gridLayout_6.addWidget(self.pushButtonStopSignalSending, 2, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.EndlessSendingradioButton = QtWidgets.QRadioButton(self.frame_6)
        self.EndlessSendingradioButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.EndlessSendingradioButton.setObjectName("EndlessSendingradioButton")
        self.gridLayout_4.addWidget(self.EndlessSendingradioButton, 0, 0, 1, 2)
        self.SendCyclesradioButton = QtWidgets.QRadioButton(self.frame_6)
        self.SendCyclesradioButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SendCyclesradioButton.setChecked(True)
        self.SendCyclesradioButton.setObjectName("SendCyclesradioButton")
        self.gridLayout_4.addWidget(self.SendCyclesradioButton, 1, 0, 1, 2)
        self.CyclesNumberspinBox = QtWidgets.QSpinBox(self.frame_6)
        self.CyclesNumberspinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.CyclesNumberspinBox.setMinimum(1)
        self.CyclesNumberspinBox.setMaximum(10000)
        self.CyclesNumberspinBox.setObjectName("CyclesNumberspinBox")
        self.gridLayout_4.addWidget(self.CyclesNumberspinBox, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_6, 1, 0, 1, 1)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_5)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.frame_4)
        self.gridLayout_5.addWidget(self.frame_7, 0, 0, 3, 1)
        self.plot_widget = PlotCanvas(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy)
        self.plot_widget.setMinimumSize(QtCore.QSize(300, 200))
        self.plot_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plot_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plot_widget.setObjectName("plot_widget")
        self.gridLayout_5.addWidget(self.plot_widget, 0, 1, 3, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Config Filename:"))
        self.ConfigFileNamelineEdit.setText(_translate("MainWindow", "Example"))
        self.AutoFillpushButton.setText(_translate("MainWindow", "Auto-Fill"))
        self.label_3.setText(_translate("MainWindow", "Log filename:"))
        self.LogFilenamelineEdit.setText(_translate("MainWindow", "ScheduleLogs/Default"))
        self.label_2.setText(_translate("MainWindow", "Experiment\n"
                                                      "completeness, %:"))
        self.pushButtonStartSignalSending.setText(_translate("MainWindow", "Start"))
        self.PauseSendingradioButton.setText(_translate("MainWindow", "Pause"))
        self.ResumeSendingradioButton.setText(_translate("MainWindow", "Resume"))
        self.pushButtonStopSignalSending.setText(_translate("MainWindow", "Stop"))
        self.EndlessSendingradioButton.setText(_translate("MainWindow", "Send Continuously"))
        self.SendCyclesradioButton.setText(_translate("MainWindow", "Send Cycles"))
        self.label.setText(_translate("MainWindow", "Cycles №"))


from PlotCanvas import PlotCanvas
