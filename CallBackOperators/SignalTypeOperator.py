from CallBackOperator import CallBackOperator
from PyQt5 import QtWidgets

class Test(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.InitAloitus()

    def InitAloitus(self):
        self.button = QtWidgets.QPushButton("Ok", self)
        self.button.move(200, 200)
        self.button.clicked.connect(self.continue2)
        self.setGeometry(600, 200, 500, 300)
        self.show()


    def continue2(self):
        print('callback')
        #self.close()
        #self.next = Second()
        # next.__init__()
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)


class SignalTypeOperator(CallBackOperator):
    def __init__(self):
        self.UserInterface = None
        self.MainWindow = None

    def SetMainWindow(self, MainWindow):
        self.MainWindow = MainWindow

    def ConnectCallBack(self, UserInterface):
        UserInterface.SignalTypecomboBox.currentIndexChanged.connect(self.SetSignalType)
        self.UserInterface = UserInterface

    def SetSignalType(self):
        print('in callback')
        #self.dialog = QtWidgets.QDialog(self.MainWindow)
        #self.dialog.show()
        self.Test = Test()
        #self.dialog.setModal(True)
        #self.dialog.exec()

        #MainWindow.count = MainWindow.count + 1
        #sub =QtWidgets.QMdiSubWindow()
        #sub.setWidget(QtWidgets.QTextEdit())
        #sub.setWindowTitle("subwindow" + str(MainWindow.count))
        #self.mdi.addSubWindow(sub)
        #sub.show()

        #win = Test() #QtWidgets.QMainWindow()
        #win.show()



class Aloitus(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitAloitus()

    def InitAloitus(self):
        self.button=QtWidgets.QPushButton("Ok",self)
        self.button.move(200,200)
        self.button.clicked.connect(self.continue2)
        self.setGeometry(600,200,500,300)
        self.show()

    def continue2(self):
        #self.close()
        print('child window callback')
        self.next=Second()
        #next.__init__()

class Second(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title="Alkutiedot"
        self.top=600
        self.left=200
        self.width=500
        self.height=500

        self.initWindow()

    def initWindow(self):

        self.button=QtWidgets.QPushButton("Ok", self)
        self.button.move(100,400)
        self.button.clicked.connect(self.ok)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def ok(self):
        print('close clicked')
        self.close()


