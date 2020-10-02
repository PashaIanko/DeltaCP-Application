from threading import Thread, Event, Timer
import time


class SignalTimer(Thread):
    def __init__(self, interval, function):
        self.interval = interval
        self.function = function
        self.timer = Timer(self.interval, self.function)
        self.if_started = False

    def run(self):
        if self.if_started == False:
            self.timer.start()
            self.if_started = True

    def reset(self, new_interval):
        self.timer.cancel()
        self.interval = new_interval
        self.timer = Timer(self.interval, self.function)
        self.timer.start()
