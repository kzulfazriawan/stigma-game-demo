from core import Files
from library.stigma.application import Image
from library.stigma.helper import kivyBuilder, animation
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gameimagepersoneone.kv')


class GameImagepersoneone(Image):
    def __init__(self):
        super(GameImagepersoneone, self).__init__()
        self.opacity = 0

    def focus(self, source, position):
        self.opacity = 1
        self.source  = source
        self.pos     = position
        self.size    = (325, 585)

    def blink(self, run = False):
        if run:
            self.opacity = 0
            animation(self, ({'opacity': 1, 'd': .15},))

    def join(self, run = False):
        if run:
            self.opacity = 0
            x_pos = self.x
            self.x -= 100

            animation(self, ({'x': x_pos, 'd': .1}, {'opacity': 1, 'd': .15}))

    def leave(self, run = False):
        if run:
            self.opacity = 1
            animation(self, ({'x': self.x - 100, 'd': .05}, {'opacity': 0, 'd': .15}))

    def reset(self):
        self.opacity = 0
        self.size    = (0, 0)