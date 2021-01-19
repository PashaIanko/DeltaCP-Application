from ApplicationManager import ApplicationManager
from PyQt5 import QtWidgets
import Loggers
from Loggers import loggers


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Loggers.init_loggers()
    try:
        MainWindow = ApplicationManager()
    except:
        print(sys.exc_info())


    MainWindow.show()
    loggers['Application'].info('Exiting application!')
    loggers['Debug'].debug('SHIT')
    loggers['SignalSending'].info('Signal Sending finished!')

    sys.exit(app.exec_())