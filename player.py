from time import time

class Player():
    def __init__(self, x, y, sid):
        """
        Класс персонажа игрока
        :param x:
        :param y:
        :param sid: id сессии
        """
        self.x = x
        self.y = y
        self.session_id = sid
        self.last_move_time = time()
        self.speed = 100

    def get_dict(self):
        return {'x': self.x, 'y': self.y}

    def move(self, movement):
        dt = time() - self.last_move_time
        self.last_move_time = time()
        dpath = dt * self.speed
        if movement['left']:
            self.x -= dpath
        if movement['right']:
            self.x += dpath
        if movement['up']:
            self.y -= dpath
        if movement['down']:
            self.y += dpath
