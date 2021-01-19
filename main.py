from ApplicationManager import ApplicationManager
from PyQt5 import QtWidgets
import LoggersConfig
from LoggersConfig import loggers


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoggersConfig.init_loggers()
    try:
        MainWindow = ApplicationManager()
    except:
        print(sys.exc_info())


    MainWindow.show()

    loggers['Application'].info('Exiting application!')
    sys.exit(app.exec_())