from ApplicationManager import ApplicationManager
from Logger import Logger
import logging
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    try:
        MainWindow = ApplicationManager()
    except:
        print(sys.exc_info())

    AppLogger = Logger('TestLogger', logging.INFO)
    AppLogger.Info('Abc')
    MainWindow.show()
    sys.exit(app.exec_())