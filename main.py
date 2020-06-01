
from ApplicationManager import ApplicationManager
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ApplicationManager()
    MainWindow.show()
    sys.exit(app.exec_())