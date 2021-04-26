from Loggers import Logger, SilentLogger
import logging

loggers = {}


def init_loggers():
    global loggers
    #loggers['Application'] = Logger('Application', logging.INFO, format_str="%(name)s - %(levelname)s - %(message)s")
    loggers['Application'] = SilentLogger()

    loggers['SignalSending'] = SilentLogger()
    #loggers['SignalSending'] = Logger('SignalSenging', logging.INFO)

    # loggers['Debug'] = Logger('Debug', logging.DEBUG, format_str="%(name)s - %(levelname)s - %(message)s")
    loggers['Debug'] = SilentLogger()

