from Singleton import Singleton
from threading import Thread, Event, Timer
import time


@Singleton
class SignalTimer(Thread):
    def __init__(self, interval, function):
        self.interval = interval
        self.function = function
        self.timer = Timer(self.interval, self.function)

    def run(self):
        self.timer.start()

    def reset(self, new_interval):
        self.timer.cancel()
        self.interval = new_interval
        self.timer = Timer(self.interval, self.function)
        self.timer.start()
