from abc import ABCMeta, abstractmethod

class SignalObserver(metaclass=ABCMeta):
    """
    Абстрактный суперкласс для всех наблюдателей.
    """
    def __init__(self, model, plot_canvas):
        self.model = model
        self.model.AddObserver(self)
        self.plot_canvas = plot_canvas

    def UpdateModel(self, title=''):
        self.plot_canvas.plot(
            self.model.x,
            self.model.y,
            color='blue',
            marker='.'
        )
        self.plot_canvas.setTitle(title)