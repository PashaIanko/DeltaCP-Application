import logging


class Logger:
    def __init__(self, LoggerName, LogLevel, FileName=None):
        self.Logger = logging.getLogger(LoggerName)
        self.Logger.setLevel(LogLevel)

        if FileName is not None:
            self.Handler = logging.FileHandler(FileName + '.log')
        else:
            import sys
            self.Handler = logging.StreamHandler(sys.stdout)

        self.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.Handler.setFormatter(self.Formatter)
        self.Logger.addHandler(self.Handler)

    def info(self, msg):
        self.Logger.info(msg)

    def debug(self, msg):
        self.Logger.debug(msg)

    def Warning(self, msg):
        self.Logger.warning(msg)