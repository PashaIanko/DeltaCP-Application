from PyQt5 import QtCore, QtWidgets, QtGui


class Ui_UserSignalWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(700, 400))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(850, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ConfigFilenamelabel = QtWidgets.QLabel(self.frame_3)
        self.ConfigFilenamelabel.setLineWidth(4)
        self.ConfigFilenamelabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ConfigFilenamelabel.setObjectName("ConfigFilenamelabel")
        self.horizontalLayout.addWidget(self.ConfigFilenamelabel)
        self.ConfigFileNamelineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.ConfigFileNamelineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.ConfigFileNamelineEdit.setObjectName("ConfigFileNamelineEdit")
        self.horizontalLayout.addWidget(self.ConfigFileNamelineEdit)
        self.AutoFillpushButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AutoFillpushButton.sizePolicy().hasHeightForWidth())
        self.AutoFillpushButton.setSizePolicy(sizePolicy)
        self.AutoFillpushButton.setObjectName("AutoFillpushButton")
        self.horizontalLayout.addWidget(self.AutoFillpushButton)
        self.SavePresetpushButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SavePresetpushButton.sizePolicy().hasHeightForWidth())
        self.SavePresetpushButton.setSizePolicy(sizePolicy)
        self.SavePresetpushButton.setObjectName("SavePresetpushButton")
        self.horizontalLayout.addWidget(self.SavePresetpushButton)
        self.DeletePresetpushButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeletePresetpushButton.sizePolicy().hasHeightForWidth())
        self.DeletePresetpushButton.setSizePolicy(sizePolicy)
        self.DeletePresetpushButton.setObjectName("DeletePresetpushButton")
        self.horizontalLayout.addWidget(self.DeletePresetpushButton)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_3)
        self.lcdNumber.setMinimumSize(QtCore.QSize(100, 40))
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setMaximumSize(QtCore.QSize(500, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelStartTime = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStartTime.sizePolicy().hasHeightForWidth())
        self.labelStartTime.setSizePolicy(sizePolicy)
        self.labelStartTime.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelStartTime.setObjectName("labelStartTime")
        self.gridLayout.addWidget(self.labelStartTime, 0, 0, 1, 1)
        self.StartTimehorizontalSlider = QtWidgets.QSlider(self.frame)
        self.StartTimehorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.StartTimehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.StartTimehorizontalSlider.setObjectName("StartTimehorizontalSlider")
        self.gridLayout.addWidget(self.StartTimehorizontalSlider, 0, 1, 1, 1)
        self.StartTimelineEdit = QtWidgets.QLineEdit(self.frame)
        self.StartTimelineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.StartTimelineEdit.setObjectName("StartTimelineEdit")
        self.gridLayout.addWidget(self.StartTimelineEdit, 0, 2, 1, 1)
        self.labelAccelerationTime = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAccelerationTime.sizePolicy().hasHeightForWidth())
        self.labelAccelerationTime.setSizePolicy(sizePolicy)
        self.labelAccelerationTime.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelAccelerationTime.setObjectName("labelAccelerationTime")
        self.gridLayout.addWidget(self.labelAccelerationTime, 1, 0, 1, 1)
        self.AccelerationTimehorizontalSlider = QtWidgets.QSlider(self.frame)
        self.AccelerationTimehorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.AccelerationTimehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AccelerationTimehorizontalSlider.setObjectName("AccelerationTimehorizontalSlider")
        self.gridLayout.addWidget(self.AccelerationTimehorizontalSlider, 1, 1, 1, 1)
        self.AccelerationTimelineEdit = QtWidgets.QLineEdit(self.frame)
        self.AccelerationTimelineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.AccelerationTimelineEdit.setObjectName("AccelerationTimelineEdit")
        self.gridLayout.addWidget(self.AccelerationTimelineEdit, 1, 2, 1, 1)
        self.labelPlateauTime = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPlateauTime.sizePolicy().hasHeightForWidth())
        self.labelPlateauTime.setSizePolicy(sizePolicy)
        self.labelPlateauTime.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelPlateauTime.setObjectName("labelPlateauTime")
        self.gridLayout.addWidget(self.labelPlateauTime, 2, 0, 1, 1)
        self.PlateauTimehorizontalSlider = QtWidgets.QSlider(self.frame)
        self.PlateauTimehorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.PlateauTimehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PlateauTimehorizontalSlider.setObjectName("PlateauTimehorizontalSlider")
        self.gridLayout.addWidget(self.PlateauTimehorizontalSlider, 2, 1, 1, 1)
        self.PlateauTimelineEdit = QtWidgets.QLineEdit(self.frame)
        self.PlateauTimelineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PlateauTimelineEdit.setObjectName("PlateauTimelineEdit")
        self.gridLayout.addWidget(self.PlateauTimelineEdit, 2, 2, 1, 1)
        self.labelDecelerationTime = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDecelerationTime.sizePolicy().hasHeightForWidth())
        self.labelDecelerationTime.setSizePolicy(sizePolicy)
        self.labelDecelerationTime.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelDecelerationTime.setObjectName("labelDecelerationTime")
        self.gridLayout.addWidget(self.labelDecelerationTime, 3, 0, 1, 1)
        self.DecelerationTimehorizontalSlider = QtWidgets.QSlider(self.frame)
        self.DecelerationTimehorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.DecelerationTimehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.DecelerationTimehorizontalSlider.setObjectName("DecelerationTimehorizontalSlider")
        self.gridLayout.addWidget(self.DecelerationTimehorizontalSlider, 3, 1, 1, 1)
        self.DecelerationTimelineEdit = QtWidgets.QLineEdit(self.frame)
        self.DecelerationTimelineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.DecelerationTimelineEdit.setObjectName("DecelerationTimelineEdit")
        self.gridLayout.addWidget(self.DecelerationTimelineEdit, 3, 2, 1, 1)
        self.labeLowLevelFrequency = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labeLowLevelFrequency.sizePolicy().hasHeightForWidth())
        self.labeLowLevelFrequency.setSizePolicy(sizePolicy)
        self.labeLowLevelFrequency.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labeLowLevelFrequency.setObjectName("labeLowLevelFrequency")
        self.gridLayout.addWidget(self.labeLowLevelFrequency, 4, 0, 1, 1)
        self.LowLevelFrequencyhorizontalSlider = QtWidgets.QSlider(self.frame)
        self.LowLevelFrequencyhorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LowLevelFrequencyhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.LowLevelFrequencyhorizontalSlider.setObjectName("LowLevelFrequencyhorizontalSlider")
        self.gridLayout.addWidget(self.LowLevelFrequencyhorizontalSlider, 4, 1, 1, 1)
        self.LowLevelFrequencylineEdit = QtWidgets.QLineEdit(self.frame)
        self.LowLevelFrequencylineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.LowLevelFrequencylineEdit.setObjectName("LowLevelFrequencylineEdit")
        self.gridLayout.addWidget(self.LowLevelFrequencylineEdit, 4, 2, 1, 1)
        self.labelHighLevelFrequency = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHighLevelFrequency.sizePolicy().hasHeightForWidth())
        self.labelHighLevelFrequency.setSizePolicy(sizePolicy)
        self.labelHighLevelFrequency.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelHighLevelFrequency.setObjectName("labelHighLevelFrequency")
        self.gridLayout.addWidget(self.labelHighLevelFrequency, 5, 0, 1, 1)
        self.HighLevelFrequencyhorizontalSlider = QtWidgets.QSlider(self.frame)
        self.HighLevelFrequencyhorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.HighLevelFrequencyhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HighLevelFrequencyhorizontalSlider.setObjectName("HighLevelFrequencyhorizontalSlider")
        self.gridLayout.addWidget(self.HighLevelFrequencyhorizontalSlider, 5, 1, 1, 1)
        self.HighLevelFrequencylineEdit = QtWidgets.QLineEdit(self.frame)
        self.HighLevelFrequencylineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.HighLevelFrequencylineEdit.setObjectName("HighLevelFrequencylineEdit")
        self.gridLayout.addWidget(self.HighLevelFrequencylineEdit, 5, 2, 1, 1)
        self.labelVerticalOffset = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelVerticalOffset.sizePolicy().hasHeightForWidth())
        self.labelVerticalOffset.setSizePolicy(sizePolicy)
        self.labelVerticalOffset.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelVerticalOffset.setObjectName("labelVerticalOffset")
        self.gridLayout.addWidget(self.labelVerticalOffset, 6, 0, 1, 1)
        self.VerticalOffsethorizontalSlider = QtWidgets.QSlider(self.frame)
        self.VerticalOffsethorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.VerticalOffsethorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VerticalOffsethorizontalSlider.setObjectName("VerticalOffsethorizontalSlider")
        self.gridLayout.addWidget(self.VerticalOffsethorizontalSlider, 6, 1, 1, 1)
        self.VerticalOffsetlineEdit = QtWidgets.QLineEdit(self.frame)
        self.VerticalOffsetlineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.VerticalOffsetlineEdit.setObjectName("VerticalOffsetlineEdit")
        self.gridLayout.addWidget(self.VerticalOffsetlineEdit, 6, 2, 1, 1)
        self.labelPointsDensity = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPointsDensity.sizePolicy().hasHeightForWidth())
        self.labelPointsDensity.setSizePolicy(sizePolicy)
        self.labelPointsDensity.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelPointsDensity.setObjectName("labelPointsDensity")
        self.gridLayout.addWidget(self.labelPointsDensity, 7, 0, 1, 1)
        self.PointsNumberhorizontalSlider = QtWidgets.QSlider(self.frame)
        self.PointsNumberhorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.PointsNumberhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.PointsNumberhorizontalSlider.setObjectName("PointsNumberhorizontalSlider")
        self.gridLayout.addWidget(self.PointsNumberhorizontalSlider, 7, 1, 1, 1)
        self.PointsNumberlineEdit = QtWidgets.QLineEdit(self.frame)
        self.PointsNumberlineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PointsNumberlineEdit.setObjectName("PointsNumberlineEdit")
        self.gridLayout.addWidget(self.PointsNumberlineEdit, 7, 2, 1, 1)
        self.labelEndTime = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelEndTime.sizePolicy().hasHeightForWidth())
        self.labelEndTime.setSizePolicy(sizePolicy)
        self.labelEndTime.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelEndTime.setObjectName("labelEndTime")
        self.gridLayout.addWidget(self.labelEndTime, 8, 0, 1, 1)
        self.EndTimehorizontalSlider = QtWidgets.QSlider(self.frame)
        self.EndTimehorizontalSlider.setMaximumSize(QtCore.QSize(200, 16777215))
        self.EndTimehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EndTimehorizontalSlider.setObjectName("EndTimehorizontalSlider")
        self.gridLayout.addWidget(self.EndTimehorizontalSlider, 8, 1, 1, 1)
        self.EndTimelineEdit = QtWidgets.QLineEdit(self.frame)
        self.EndTimelineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.EndTimelineEdit.setObjectName("EndTimelineEdit")
        self.gridLayout.addWidget(self.EndTimelineEdit, 8, 2, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButtonStartSignalSending = QtWidgets.QPushButton(self.frame_6)
        self.pushButtonStartSignalSending.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButtonStartSignalSending.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStartSignalSending.setObjectName("pushButtonStartSignalSending")
        self.gridLayout_3.addWidget(self.pushButtonStartSignalSending, 0, 0, 1, 2)
        self.PauseSendingradioButton = QtWidgets.QRadioButton(self.frame_6)
        self.PauseSendingradioButton.setObjectName("PauseSendingradioButton")
        self.gridLayout_3.addWidget(self.PauseSendingradioButton, 1, 0, 1, 1)
        self.ResumeSendingradioButton = QtWidgets.QRadioButton(self.frame_6)
        self.ResumeSendingradioButton.setChecked(True)
        self.ResumeSendingradioButton.setAutoExclusive(True)
        self.ResumeSendingradioButton.setObjectName("ResumeSendingradioButton")
        self.gridLayout_3.addWidget(self.ResumeSendingradioButton, 1, 1, 1, 1)
        self.pushButtonStopSignalSending = QtWidgets.QPushButton(self.frame_6)
        self.pushButtonStopSignalSending.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButtonStopSignalSending.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonStopSignalSending.setObjectName("pushButtonStopSignalSending")
        self.gridLayout_3.addWidget(self.pushButtonStopSignalSending, 2, 0, 1, 2)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.EndlessSendingradioButton = QtWidgets.QRadioButton(self.frame_5)
        self.EndlessSendingradioButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.EndlessSendingradioButton.setObjectName("EndlessSendingradioButton")
        self.gridLayout_4.addWidget(self.EndlessSendingradioButton, 0, 0, 1, 2)
        self.SendCyclesradioButton = QtWidgets.QRadioButton(self.frame_5)
        self.SendCyclesradioButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SendCyclesradioButton.setChecked(True)
        self.SendCyclesradioButton.setObjectName("SendCyclesradioButton")
        self.gridLayout_4.addWidget(self.SendCyclesradioButton, 1, 0, 1, 2)
        self.CyclesNumberspinBox = QtWidgets.QSpinBox(self.frame_5)
        self.CyclesNumberspinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.CyclesNumberspinBox.setMinimum(1)
        self.CyclesNumberspinBox.setMaximum(100)
        self.CyclesNumberspinBox.setObjectName("CyclesNumberspinBox")
        self.gridLayout_4.addWidget(self.CyclesNumberspinBox, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame)
        self.plot_widget = PlotCanvas(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_widget.sizePolicy().hasHeightForWidth())
        self.plot_widget.setSizePolicy(sizePolicy)
        self.plot_widget.setMinimumSize(QtCore.QSize(300, 200))
        #self.plot_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.plot_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plot_widget.setObjectName("plot_widget")
        self.horizontalLayout_2.addWidget(self.plot_widget)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
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
        self.ConfigFilenamelabel.setText(_translate("MainWindow", "Config Filename:"))
        self.AutoFillpushButton.setText(_translate("MainWindow", "Auto-Fill"))
        self.SavePresetpushButton.setText(_translate("MainWindow", "Save Preset"))
        self.DeletePresetpushButton.setText(_translate("MainWindow", "Delete Preset"))
        self.label_2.setText(_translate("MainWindow", "Current Cycle №:"))
        self.labelStartTime.setText(_translate("MainWindow", "Start Time:"))
        self.labelAccelerationTime.setText(_translate("MainWindow", "Acceleration Time:"))
        self.labelPlateauTime.setText(_translate("MainWindow", "Plateau Time:"))
        self.labelDecelerationTime.setText(_translate("MainWindow", "Deceleration Time:"))
        self.labeLowLevelFrequency.setText(_translate("MainWindow", "Low-level Frequency:"))
        self.labelHighLevelFrequency.setText(_translate("MainWindow", "High-level Frequency:"))
        self.labelVerticalOffset.setText(_translate("MainWindow", "Vertical Offset:"))
        self.labelPointsDensity.setText(_translate("MainWindow", "Points Number"))
        self.labelEndTime.setText(_translate("MainWindow", "End Time:"))
        self.pushButtonStartSignalSending.setText(_translate("MainWindow", "Start"))
        self.PauseSendingradioButton.setText(_translate("MainWindow", "Pause"))
        self.ResumeSendingradioButton.setText(_translate("MainWindow", "Resume"))
        self.pushButtonStopSignalSending.setText(_translate("MainWindow", "Stop"))
        self.EndlessSendingradioButton.setText(_translate("MainWindow", "Send Continuously"))
        self.SendCyclesradioButton.setText(_translate("MainWindow", "Send Cycles"))
        self.label.setText(_translate("MainWindow", "Cycles №"))


from PlotCanvas import PlotCanvas