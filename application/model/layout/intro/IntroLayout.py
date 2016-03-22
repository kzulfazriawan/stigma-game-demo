from core import Files
from library.stigma.application import Box
from library.stigma.helper import animation


class IntroLayout(Box):
    def __init__(self):
        super(IntroLayout, self).__init__()

    def showing(self):
       animation(self, ({'opacity' : 1, 'd': .3},))

    def fading(self):
       animation(self, ({'opacity' : 0, 'd': .3},))
