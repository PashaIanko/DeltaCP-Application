from Logger import Logger
import logging

loggers = {}



def init_loggers():
    global loggers
    loggers['Application'] = Logger('Application', logging.INFO)
    loggers['SignalSending'] = Logger('SignalSenging', logging.INFO, FileName='SignalSending')
    loggers['Debug'] = Logger('Debug', logging.DEBUG)