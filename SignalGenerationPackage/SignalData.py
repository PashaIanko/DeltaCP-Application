from abc import ABCMeta


class SignalData(metaclass=ABCMeta):

    point_array = []
    transformed_point_array = []
    point_array_with_requests = []

    x = []
    y = []
    dx = []

    def __init__(self):
        pass