from CallBackOperator import CallBackOperator

class StartSendingOperator(CallBackOperator):

    def __init__(self):
        self.UserInterface = None  # TODO: Перенести в родительский класс UserInterface


    def ConnectCallBack(self, UserInterface):
        self.UserInterface = UserInterface
        UserInterface.pushButtonStartSignalSending.clicked.connect(self.StartSendingSignal)


    def StartSendingSignal(self):
        print(f'in callback')
        # Получить x и y модели, Сигнала