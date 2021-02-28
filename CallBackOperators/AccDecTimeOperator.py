# from CallBackOperator import CallBackOperator
# from DeltaCPClient import DeltaCPClient
# from LoggersConfig import loggers
#
# class AccDecTimeOperator(CallBackOperator):
#     def __init__(self):
#         super().__init__()
#         self.DeltaCPClient = DeltaCPClient()
#
#     def ConnectCallBack(self, window):
#         window.AccDecTime1pushButton.clicked.connect(self.RequestTimes1)
#         window.AccDecTime2pushButton.clicked.connect(self.RequestTimes2)
#         window.AccDecTime3pushButton.clicked.connect(self.RequestTimes3)
#         window.AccDecTime4pushButton.clicked.connect(self.RequestTimes4)
#
#     def RequestTimes1(self):
#         AccTime = self.DeltaCPClient.RequestAccelerationTime1()
#         DecTime = self.DeltaCPClient.RequestDecelerationTime1()
#         loggers['Debug'].debug(f'AccelerationTime1 = {AccTime}, DecelerationTime1 = {DecTime}')
#
#     def RequestTimes2(self):
#         AccTime = self.DeltaCPClient.RequestAccelerationTime2()
#         DecTime = self.DeltaCPClient.RequestDecelerationTime2()
#         loggers['Debug'].debug(f'AccelerationTime2 = {AccTime}, DecelerationTime2 = {DecTime}')
#
#     def RequestTimes3(self):
#         AccTime = self.DeltaCPClient.RequestAccelerationTime3()
#         DecTime = self.DeltaCPClient.RequestDecelerationTime3()
#         loggers['Debug'].debug(f'AccelerationTime3 = {AccTime}, DecelerationTime3 = {DecTime}')
#
#     def RequestTimes4(self):
#         AccTime = self.DeltaCPClient.RequestAccelerationTime4()
#         DecTime = self.DeltaCPClient.RequestDecelerationTime4()
#         loggers['Debug'].debug(f'AccelerationTime4 = {AccTime}, DecelerationTime4 = {DecTime}')