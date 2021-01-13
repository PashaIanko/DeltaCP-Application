import SignalGenerationPackage.SignalData
from SignalSendingPackage.SignalSendingOperator import SignalSendingOperator


class ForwardSendingOperator(SignalSendingOperator):

    # Реализует отправку "наперёд". На графика сигнала, по оси икс - моменты времени
    # по Y - какое значение сигнала отправить. В текущий момент времени T отправляется
    # не текущее значение сигнала, а то, что соответствует следующему моменту времени.
    # Таким образом, нет гарантий, но вероятность больше, что в каждый момент T
    # Будет достигнута истинная частота Y, указанная на графике для этого момента времени
    # (А не просто выставлена в этот момент времени)

    def __init__(self):
        super().__init__()

    # overridden
    def ExecuteSending(self, Time):
        pass
