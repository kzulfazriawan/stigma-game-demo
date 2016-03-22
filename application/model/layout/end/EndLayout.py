from library.stigma.helper import animation
from library.stigma.application import Float


class EndLayout(Float):
    def __init__(self):
        super(EndLayout, self).__init__()

    def showing(self):
       animation(self, ({'opacity' : 1, 'd': .2},))

    def fading(self):
       animation(self, ({'opacity' : 1, 'd': .2},))