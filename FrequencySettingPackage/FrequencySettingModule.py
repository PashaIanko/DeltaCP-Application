from ApplicationModule import ApplicationModule


class FrequencySettingModule(ApplicationModule):

    callback_operators = \
        [

        ]

    def __init__(self):
        self.window = None



    def Run(self, MainWindow):
        self.UserInterface = MainWindow.ui
        self.MainWindow = MainWindow
        self.ConnectAllCallBacks()  # TODO: Перенести этот код в родителя


    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.UserInterface)  # TODO: код в родителя

