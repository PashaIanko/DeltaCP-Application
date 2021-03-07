from dataclasses import dataclass

@dataclass
class Point:
    y: float  # Задаваемая частота
    x: float  # Время
    to_send: bool  # Отправляем или запрашиваем