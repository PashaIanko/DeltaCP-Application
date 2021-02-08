from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QtCore.QSize(800, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aaa = QtWidgets.QTabWidget(self.centralwidget)
        self.aaa.setObjectName("aaa")
        self.ConnectionParametersTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConnectionParametersTab.sizePolicy().hasHeightForWidth())
        self.ConnectionParametersTab.setSizePolicy(sizePolicy)
        self.ConnectionParametersTab.setMinimumSize(QtCore.QSize(0, 400))
        self.ConnectionParametersTab.setObjectName("ConnectionParametersTab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.ConnectionParametersTab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_16 = QtWidgets.QFrame(self.ConnectionParametersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_15 = QtWidgets.QFrame(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setMinimumSize(QtCore.QSize(200, 200))
        self.frame_15.setMaximumSize(QtCore.QSize(400, 400))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_15)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.ProtocolcomboBox = QtWidgets.QComboBox(self.frame_15)
        self.ProtocolcomboBox.setObjectName("ProtocolcomboBox")
        self.ProtocolcomboBox.addItem("")
        self.ProtocolcomboBox.setItemText(0, "")
        self.ProtocolcomboBox.addItem("")
        self.ProtocolcomboBox.addItem("")
        self.gridLayout_2.addWidget(self.ProtocolcomboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_15)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.ByteSizecomboBox = QtWidgets.QComboBox(self.frame_15)
        self.ByteSizecomboBox.setObjectName("ByteSizecomboBox")
        self.ByteSizecomboBox.addItem("")
        self.ByteSizecomboBox.setItemText(0, "")
        self.ByteSizecomboBox.addItem("")
        self.ByteSizecomboBox.addItem("")
        self.gridLayout_2.addWidget(self.ByteSizecomboBox, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_15)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.ParitycomboBox = QtWidgets.QComboBox(self.frame_15)
        self.ParitycomboBox.setObjectName("ParitycomboBox")
        self.ParitycomboBox.addItem("")
        self.ParitycomboBox.setItemText(0, "")
        self.ParitycomboBox.addItem("")
        self.ParitycomboBox.addItem("")
        self.ParitycomboBox.addItem("")
        self.gridLayout_2.addWidget(self.ParitycomboBox, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_15)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.StopBitscomboBox = QtWidgets.QComboBox(self.frame_15)
        self.StopBitscomboBox.setObjectName("StopBitscomboBox")
        self.StopBitscomboBox.addItem("")
        self.StopBitscomboBox.setItemText(0, "")
        self.StopBitscomboBox.addItem("")
        self.StopBitscomboBox.addItem("")
        self.gridLayout_2.addWidget(self.StopBitscomboBox, 3, 1, 1, 1)
        self.ComPortNumberlabel = QtWidgets.QLabel(self.frame_15)
        self.ComPortNumberlabel.setObjectName("ComPortNumberlabel")
        self.gridLayout_2.addWidget(self.ComPortNumberlabel, 4, 0, 1, 1)
        self.COMPortcomboBox = QtWidgets.QComboBox(self.frame_15)
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
        self.gridLayout_2.addWidget(self.COMPortcomboBox, 4, 1, 1, 1)
        self.BaudRateLabel = QtWidgets.QLabel(self.frame_15)
        self.BaudRateLabel.setObjectName("BaudRateLabel")
        self.gridLayout_2.addWidget(self.BaudRateLabel, 5, 0, 1, 1)
        self.BaudRatecomboBox = QtWidgets.QComboBox(self.frame_15)
        self.BaudRatecomboBox.setObjectName("BaudRatecomboBox")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.setItemText(0, "")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.addItem("")
        self.BaudRatecomboBox.addItem("")
        self.gridLayout_2.addWidget(self.BaudRatecomboBox, 5, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_15)
        self.frame = QtWidgets.QFrame(self.frame_16)
        self.frame.setMaximumSize(QtCore.QSize(300, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.AutoConnectpushButton = QtWidgets.QPushButton(self.frame)
        self.AutoConnectpushButton.setObjectName("AutoConnectpushButton")
        self.horizontalLayout_7.addWidget(self.AutoConnectpushButton)
        self.ConnectpushButton = QtWidgets.QPushButton(self.frame)
        self.ConnectpushButton.setObjectName("ConnectpushButton")
        self.horizontalLayout_7.addWidget(self.ConnectpushButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_8.addWidget(self.frame_16, 0, 0, 1, 1)
        self.frame_17 = QtWidgets.QFrame(self.ConnectionParametersTab)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_8.addWidget(self.frame_17, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem, 1, 0, 1, 1)
        self.aaa.addTab(self.ConnectionParametersTab, "")
        self.OutputFrequencySettingTab = QtWidgets.QWidget()
        self.OutputFrequencySettingTab.setObjectName("OutputFrequencySettingTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.OutputFrequencySettingTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_22 = QtWidgets.QFrame(self.OutputFrequencySettingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_22.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_21 = QtWidgets.QFrame(self.frame_22)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_5 = QtWidgets.QFrame(self.frame_21)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.RequestSetFrequencypushButton = QtWidgets.QPushButton(self.frame_5)
        self.RequestSetFrequencypushButton.setObjectName("RequestSetFrequencypushButton")
        self.verticalLayout_4.addWidget(self.RequestSetFrequencypushButton)
        self.SetFrequencypushButton = QtWidgets.QPushButton(self.frame_5)
        self.SetFrequencypushButton.setObjectName("SetFrequencypushButton")
        self.verticalLayout_4.addWidget(self.SetFrequencypushButton)
        self.RequestCurrentFrequencypushButton = QtWidgets.QPushButton(self.frame_5)
        self.RequestCurrentFrequencypushButton.setObjectName("RequestCurrentFrequencypushButton")
        self.verticalLayout_4.addWidget(self.RequestCurrentFrequencypushButton)
        self.horizontalLayout_11.addWidget(self.frame_5)
        self.frame_3 = QtWidgets.QFrame(self.frame_21)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.StopFrequencypushButton = QtWidgets.QPushButton(self.frame_3)
        self.StopFrequencypushButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.StopFrequencypushButton.setObjectName("StopFrequencypushButton")
        self.horizontalLayout_12.addWidget(self.StopFrequencypushButton)
        self.StartFrequencypushButton = QtWidgets.QPushButton(self.frame_3)
        self.StartFrequencypushButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.StartFrequencypushButton.setObjectName("StartFrequencypushButton")
        self.horizontalLayout_12.addWidget(self.StartFrequencypushButton)
        self.horizontalLayout_11.addWidget(self.frame_3)
        self.gridLayout_5.addWidget(self.frame_21, 1, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_19.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.OutputFrequencylineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.OutputFrequencylineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.OutputFrequencylineEdit.setObjectName("OutputFrequencylineEdit")
        self.horizontalLayout_3.addWidget(self.OutputFrequencylineEdit)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.FrequencySetSlider = QtWidgets.QSlider(self.frame_2)
        self.FrequencySetSlider.setMaximum(50)
        self.FrequencySetSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FrequencySetSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.FrequencySetSlider.setObjectName("FrequencySetSlider")
        self.horizontalLayout.addWidget(self.FrequencySetSlider)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.gridLayout_5.addWidget(self.frame_19, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_22, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 2, 1, 1, 1)
        self.aaa.addTab(self.OutputFrequencySettingTab, "")
        self.FrequencySignalSetting = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrequencySignalSetting.sizePolicy().hasHeightForWidth())
        self.FrequencySignalSetting.setSizePolicy(sizePolicy)
        self.FrequencySignalSetting.setMaximumSize(QtCore.QSize(16777215, 500))
        self.FrequencySignalSetting.setObjectName("FrequencySignalSetting")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.FrequencySignalSetting)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_7 = QtWidgets.QFrame(self.FrequencySignalSetting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 140))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_20 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_18 = QtWidgets.QFrame(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QtCore.QSize(100, 50))
        self.frame_18.setMaximumSize(QtCore.QSize(300, 100))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_18)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.SignalTypecomboBox = QtWidgets.QComboBox(self.frame_18)
        self.SignalTypecomboBox.setObjectName("SignalTypecomboBox")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.setItemText(0, "")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.addItem("")
        self.SignalTypecomboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.SignalTypecomboBox)
        self.verticalLayout.addWidget(self.frame_18)
        self.frame_9 = QtWidgets.QFrame(self.frame_20)
        self.frame_9.setMinimumSize(QtCore.QSize(100, 60))
        self.frame_9.setMaximumSize(QtCore.QSize(300, 100))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.AccelerationTimelabel_2 = QtWidgets.QLabel(self.frame_9)
        self.AccelerationTimelabel_2.setObjectName("AccelerationTimelabel_2")
        self.horizontalLayout_5.addWidget(self.AccelerationTimelabel_2)
        self.AccDec1radioButton = QtWidgets.QRadioButton(self.frame_9)
        self.AccDec1radioButton.setChecked(True)
        self.AccDec1radioButton.setObjectName("AccDec1radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec1radioButton)
        self.AccDec2radioButton = QtWidgets.QRadioButton(self.frame_9)
        self.AccDec2radioButton.setObjectName("AccDec2radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec2radioButton)
        self.AccDec3radioButton = QtWidgets.QRadioButton(self.frame_9)
        self.AccDec3radioButton.setObjectName("AccDec3radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec3radioButton)
        self.AccDec4radioButton = QtWidgets.QRadioButton(self.frame_9)
        self.AccDec4radioButton.setObjectName("AccDec4radioButton")
        self.horizontalLayout_5.addWidget(self.AccDec4radioButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.frame_9)
        self.horizontalLayout_10.addWidget(self.frame_20)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout.addWidget(self.frame_8, 0, 1, 1, 1)
        self.horizontalLayout_9.addWidget(self.frame_7)
        self.aaa.addTab(self.FrequencySignalSetting, "")
        self.SignalSendingTab = QtWidgets.QWidget()
        self.SignalSendingTab.setObjectName("SignalSendingTab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.SignalSendingTab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.SignalSendingTab)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonStartSignalSending = QtWidgets.QPushButton(self.frame_12)
        self.pushButtonStartSignalSending.setObjectName("pushButtonStartSignalSending")
        self.horizontalLayout_6.addWidget(self.pushButtonStartSignalSending)
        self.EndlessSendingcheckBox = QtWidgets.QCheckBox(self.frame_12)
        self.EndlessSendingcheckBox.setObjectName("EndlessSendingcheckBox")
        self.horizontalLayout_6.addWidget(self.EndlessSendingcheckBox)
        self.gridLayout_7.addWidget(self.frame_12, 0, 0, 1, 2)
        self.frame_11 = QtWidgets.QFrame(self.SignalSendingTab)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_7.addWidget(self.frame_11, 0, 2, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.SignalSendingTab)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.PauseSendingradioButton = QtWidgets.QRadioButton(self.frame_10)
        self.PauseSendingradioButton.setObjectName("PauseSendingradioButton")
        self.gridLayout_6.addWidget(self.PauseSendingradioButton, 0, 0, 1, 1)
        self.ResumeSendingradioButton = QtWidgets.QRadioButton(self.frame_10)
        self.ResumeSendingradioButton.setChecked(True)
        self.ResumeSendingradioButton.setAutoExclusive(True)
        self.ResumeSendingradioButton.setObjectName("ResumeSendingradioButton")
        self.gridLayout_6.addWidget(self.ResumeSendingradioButton, 0, 1, 1, 1)
        self.pushButtonStopSignalSending = QtWidgets.QPushButton(self.frame_10)
        self.pushButtonStopSignalSending.setObjectName("pushButtonStopSignalSending")
        self.gridLayout_6.addWidget(self.pushButtonStopSignalSending, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_10, 1, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.SignalSendingTab)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_7.addWidget(self.frame_13, 1, 1, 1, 1)
        self.frame_14 = QtWidgets.QFrame(self.SignalSendingTab)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_7.addWidget(self.frame_14, 1, 2, 1, 1)
        self.aaa.addTab(self.SignalSendingTab, "")
        self.gridLayout_3.addWidget(self.aaa, 0, 0, 1, 1)
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
        self.label.setText(_translate("MainWindow", "Protocol:"))
        self.ProtocolcomboBox.setItemText(1, _translate("MainWindow", "rtu"))
        self.ProtocolcomboBox.setItemText(2, _translate("MainWindow", "ascii"))
        self.label_2.setText(_translate("MainWindow", "Byte size"))
        self.ByteSizecomboBox.setItemText(1, _translate("MainWindow", "7"))
        self.ByteSizecomboBox.setItemText(2, _translate("MainWindow", "8"))
        self.label_5.setText(_translate("MainWindow", "Parity:"))
        self.ParitycomboBox.setItemText(1, _translate("MainWindow", "O"))
        self.ParitycomboBox.setItemText(2, _translate("MainWindow", "N"))
        self.ParitycomboBox.setItemText(3, _translate("MainWindow", "E"))
        self.label_6.setText(_translate("MainWindow", "Stop Bits:"))
        self.StopBitscomboBox.setItemText(1, _translate("MainWindow", "1"))
        self.StopBitscomboBox.setItemText(2, _translate("MainWindow", "2"))
        self.ComPortNumberlabel.setText(_translate("MainWindow", "COM Port Number:"))
        self.COMPortcomboBox.setItemText(1, _translate("MainWindow", "COM1"))
        self.COMPortcomboBox.setItemText(2, _translate("MainWindow", "COM2"))
        self.COMPortcomboBox.setItemText(3, _translate("MainWindow", "COM3"))
        self.COMPortcomboBox.setItemText(4, _translate("MainWindow", "COM4"))
        self.COMPortcomboBox.setItemText(5, _translate("MainWindow", "COM5"))
        self.COMPortcomboBox.setItemText(6, _translate("MainWindow", "COM6"))
        self.COMPortcomboBox.setItemText(7, _translate("MainWindow", "COM7"))
        self.BaudRateLabel.setText(_translate("MainWindow", "Baud Rate: "))
        self.BaudRatecomboBox.setItemText(1, _translate("MainWindow", "1200"))
        self.BaudRatecomboBox.setItemText(2, _translate("MainWindow", "2400"))
        self.BaudRatecomboBox.setItemText(3, _translate("MainWindow", "3600"))
        self.BaudRatecomboBox.setItemText(4, _translate("MainWindow", "9600"))
        self.AutoConnectpushButton.setText(_translate("MainWindow", "Auto-Connect"))
        self.ConnectpushButton.setText(_translate("MainWindow", "Connect"))
        self.aaa.setTabText(self.aaa.indexOf(self.ConnectionParametersTab),
                            _translate("MainWindow", "Connection Parameters"))
        self.RequestSetFrequencypushButton.setText(_translate("MainWindow", "Request Set \n"
                                                                            "Frequency"))
        self.SetFrequencypushButton.setText(_translate("MainWindow", "Set frequency"))
        self.RequestCurrentFrequencypushButton.setText(_translate("MainWindow", "Request Current\n"
                                                                                "Frequency"))
        self.StopFrequencypushButton.setText(_translate("MainWindow", "Stop"))
        self.StartFrequencypushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Output frequency:"))
        self.OutputFrequencylineEdit.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "100"))
        self.aaa.setTabText(self.aaa.indexOf(self.OutputFrequencySettingTab),
                            _translate("MainWindow", "Output Frequency Setting"))
        self.label_4.setText(_translate("MainWindow", "Signal type:"))
        self.SignalTypecomboBox.setItemText(1, _translate("MainWindow", "sin"))
        self.SignalTypecomboBox.setItemText(2, _translate("MainWindow", "user signal"))
        self.SignalTypecomboBox.setItemText(3, _translate("MainWindow", "dynamic points density"))
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
        self.EndlessSendingcheckBox.setText(_translate("MainWindow", "Send Pattern Continuously"))
        self.PauseSendingradioButton.setText(_translate("MainWindow", "Pause"))
        self.ResumeSendingradioButton.setText(_translate("MainWindow", "Resume"))
        self.pushButtonStopSignalSending.setText(_translate("MainWindow", "Stop Sending"))
        self.aaa.setTabText(self.aaa.indexOf(self.SignalSendingTab),
                            _translate("MainWindow", "Signal Sending to Delta PC"))
        self.menuConnection_Parameters.setTitle(_translate("MainWindow", "Connection Parameters"))
        self.menuOutput_Frequency_Settings.setTitle(_translate("MainWindow", "Output Frequency Settings"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))