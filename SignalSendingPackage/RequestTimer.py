# from SignalSendingPackage.SignalTimer import SignalTimer
# from threading import Thread
# import numpy as np
# from LoggersConfig import loggers
#
# class RequestTimer(SignalTimer):
#     def __init__(self, interval, function, request_freq):
#         super().__init__(interval, function)
#         self.request_freq = request_freq
#         self.time_to = 0
#         self.time_from = 0
#         self.dt = 0
#         self.request_thread = None
#         self.time_stamp = self.time_from  # В какой момент времени на графике выставить опрошенную частоту. Перевчитывается
#                                             # в RequestFunc
#         self.frequency_requested = False
#
#
#     def launch_request_thread(self):
#         self.request_thread = Thread(target=self.RequestFunc)
#         self.request_thread.start()
#         return
#
#     def RequestFunc(self):
#         # Это функция, исполняющаяся в отдельном потоке. Суть в том, чтобы за dt (это dt которое
#         # ждёт SignalTimer чтобы отправить сигнал), запустить и завершить этот поток. Опросить за это dt
#         # несколько раз истинную частоту
#
#         requests_numb = int(self.dt * self.request_freq) - 2  # Сколько раз опросить. -1, чтоб крайние
#         # точки не цеплять (рассм пример с dt = 2, request_freq = 2Гц)
#
#         loggers['SignalSending'].info(f'RequestTimer: RequestFunc: requests_num = {requests_numb}')
#         requests_and_edges = requests_numb + 2  # c учётом краёв
#         if requests_and_edges > 2: # если есть точки кроме крайних
#             t_arr = np.linspace(0, self.dt, requests_and_edges, endpoint=True)
#             delta_t = self.calc_dts(t_arr)
#
#             initial_dt = delta_t[0]
#             if self.if_started:
#                 self.reset(initial_dt)
#             else:
#                 self.interval = initial_dt
#                 self.run()
#             self.time_stamp += initial_dt
#
#
#
#             dt_iterator = 1
#             while dt_iterator < len(delta_t) - 1:
#                 if self.frequency_requested:
#                     self.frequency_requested = False
#
#                     self.interval = delta_t[dt_iterator]
#                     self.time_stamp += self.interval
#
#                     if self.if_started:  # Если уже дали старт таймеру на предудущем цикле
#                         self.reset(self.interval)
#                     else:
#                         self.run()
#
#     def calc_dts(self, arr):
#         N = len(arr)
#         delta_t = []
#         if N > 1:
#             delta_t = [
#                 arr[dt_next_idx] - arr[dt_prev_idx]
#                 for dt_next_idx, dt_prev_idx
#                 in zip(range(1, N), range(0, N - 1))
#             ]
#         return delta_t