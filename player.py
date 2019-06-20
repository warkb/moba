from time import time

from point import Point

class Player():
    def __init__(self, x, y, sid):
        """
        Класс персонажа игрока
        :param x:
        :param y:
        :param sid: id сессии
        """
        self.point = Point(x, y)
        self.session_id = sid
        self.last_move_time = time()
        self.speed = 100
        self.dest_point = None # точка, куда хочет попасть герой

    def get_dict(self):
        return {'x': self.point.x, 'y': self.point.y}

    def move(self, movement):
        dt = time() - self.last_move_time
        self.last_move_time = time()
        dpath = dt * self.speed

