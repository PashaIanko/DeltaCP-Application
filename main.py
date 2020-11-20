
from ApplicationManager import ApplicationManager
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    try:
        MainWindow = ApplicationManager()
    except:
        print(sys.exc_info())
    MainWindow.show()
    sys.exit(app.exec_())