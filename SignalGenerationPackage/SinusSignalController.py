from PyQt5 import QtWidgets
from SignalGenerationPackage.SignalController import SignalController
from PyQt5 import QtCore, QtGui

class Ui_SinWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 110, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelVerticalOffset = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelVerticalOffset.setObjectName("labelVerticalOffset")
        self.verticalLayout.addWidget(self.labelVerticalOffset)
        self.labelFrequency = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelFrequency.setObjectName("labelFrequency")
        self.verticalLayout.addWidget(self.labelFrequency)
        self.labelAmplitude = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelAmplitude.setObjectName("labelAmplitude")
        self.verticalLayout.addWidget(self.labelAmplitude)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 110, 160, 88))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEditVerticalOffset = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditVerticalOffset.setObjectName("lineEditVerticalOffset")
        self.verticalLayout_3.addWidget(self.lineEditVerticalOffset)
        self.lineEditFrequency = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditFrequency.setObjectName("lineEditFrequency")
        self.verticalLayout_3.addWidget(self.lineEditFrequency)
        self.lineEditAmplitude = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditAmplitude.setObjectName("lineEditAmplitude")
        self.verticalLayout_3.addWidget(self.lineEditAmplitude)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(490, 110, 160, 82))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalSliderVerticalOffset = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSliderVerticalOffset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderVerticalOffset.setObjectName("horizontalSliderVerticalOffset")
        self.verticalLayout_4.addWidget(self.horizontalSliderVerticalOffset)
        self.horizontalSliderFrequency = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSliderFrequency.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderFrequency.setObjectName("horizontalSliderFrequency")
        self.verticalLayout_4.addWidget(self.horizontalSliderFrequency)
        self.horizontalSliderAmplitude = QtWidgets.QSlider(self.verticalLayoutWidget_3)
        self.horizontalSliderAmplitude.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderAmplitude.setObjectName("horizontalSliderAmplitude")
        self.verticalLayout_4.addWidget(self.horizontalSliderAmplitude)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.labelVerticalOffset.setText(_translate("MainWindow", "Vertical offset"))
        self.labelFrequency.setText(_translate("MainWindow", "Frequency (w)"))
        self.labelAmplitude.setText(_translate("MainWindow", "Amplitude"))


class SinusSignalController(SignalController):

    def __init__(self):
        super().__init__()
        self.InitSignalUI()

    # overriden method - here you define personal Graphical Interface (Ui) and show the window
    def InitSignalUI(self):
        self.ui = Ui_SinWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def continue2(self):
        print('callback')