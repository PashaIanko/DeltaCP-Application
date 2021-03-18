from SignalSendingPackage.VisualizerMainWindow import VisualizerMainWindow


class SignalVisualizer:
    def __init__(self, plot_widget, x_arr=[], y_arr=[]):
        self.main_window = None  # Окно, куда будем выводить визуализацию
        # self.init_main_window()
        self.Graph = plot_widget  # self.main_window.VisualizerPlot
        self.x = x_arr
        self.y = y_arr
        self.IfRestarted = True
        self.Offset = 0.3

    def close_visualization_window(self):
        if self.main_window is not None:
            self.main_window.close()
            self.main_window = None

    def init_main_window(self):
        self.main_window = VisualizerMainWindow()
        self.main_window.show()

    def UpdateSetFrequency(self, x_val, y_val):
        if self.IfRestarted:
            self.IfRestarted = False
            self.Graph.plot(self.x, self.y, color='b', marker='.', markersize=7)
            self.Graph.add_point(x_val, y_val, color='red', marker='+', markersize=10)
        else:
            self.Graph.add_point(x_val, y_val, color='red', marker='+', markersize=10)

    def UpdateCurrentFrequency(self, x_val, y_val):
        if x_val is not None and y_val is not None:
            if self.IfRestarted:
                self.IfRestarted = False
                self.Graph.plot(self.x, self.y, color='b', marker='.', markersize=7)
                self.Graph.add_point(x_val, y_val, color='black', marker='x', markersize=7)
            else:
                self.Graph.add_point(x_val, y_val, color='black', marker='x', markersize=7)

    def Restart(self, TimeArray):
        self.Graph.clear()
        # Сейчас должны рестартануть. Поэтому, в функции self.UpdateSetFreuency(x, y)
        # Мы вызовем функцию plot().
        self.IfRestarted = True
        if len(TimeArray) != 0:
            self.x = TimeArray
            self.Graph.set_xlim(TimeArray[0] - self.Offset, TimeArray[-1] + self.Offset)

    def RefreshData(self, x, y):
        self.x = x
        self.y = y

    def check_if_window_closed(self):
        return False

        #if self.main_window is None:
        #    return True
        #return self.main_window.window_is_closed

    def ResetPlot(self):
        # Отрисовать на графике исходный сигнал
        self.Graph.plot(self.x, self.y, color='b', marker='.', markersize=7)
