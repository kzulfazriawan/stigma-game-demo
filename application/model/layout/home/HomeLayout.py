from library.stigma.helper import animation
from library.stigma.application import Float


class HomeLayout(Float):
    def __init__(self):
        super(HomeLayout, self).__init__()
        self.opacity = 0

    def showing(self):
       animation(self, ({'opacity' : 1, 'd': .1},))

    def fading(self):
       animation(self, ({'opacity' : 0, 'd': .1},))