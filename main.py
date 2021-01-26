from ApplicationManager import ApplicationManager
from PyQt5 import QtWidgets
import LoggersConfig
from LoggersConfig import loggers


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        LoggersConfig.init_loggers()
        AppManager = ApplicationManager()
        AppManager.MainWindow.show()
        sys.exit(app.exec_())
        loggers['Application'].info('Exiting application!')

    except:
        loggers['Debug'].debug(f'Main: {sys.exc_info()}')


