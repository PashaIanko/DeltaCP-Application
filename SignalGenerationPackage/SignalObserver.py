from abc import ABCMeta, abstractmethod

class SignalObserver(metaclass=ABCMeta):
    """
    Абстрактный суперкласс для всех наблюдателей.
    """
    def __init__(self, model, plot_canvas):
        self.model = model
        self.model.AddObserver(self)
        self.plot_canvas = plot_canvas

    @abstractmethod
    def UpdateModel(self):
        pass