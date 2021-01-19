import logging


class Logger:
    def __init__(self, LoggerName, LogLevel,
                 FileName=None,
                 format_str=None):
        self.Logger = logging.getLogger(LoggerName)
        self.Logger.setLevel(LogLevel)

        if FileName is not None:
            self.Handler = logging.FileHandler(FileName + '.log')
        else:
            import sys
            self.Handler = logging.StreamHandler(sys.stdout)

        if format_str is None:
            self.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        else:
            self.Formatter = logging.Formatter(format_str)

        self.Handler.setFormatter(self.Formatter)
        self.Logger.addHandler(self.Handler)

    def info(self, msg):
        self.Logger.info(msg)

    def debug(self, msg):
        self.Logger.debug(msg)

    def warning(self, msg):
        self.Logger.warning(msg)


class SilentLogger():
    def __init__(self):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def debug(self, msg):
        pass