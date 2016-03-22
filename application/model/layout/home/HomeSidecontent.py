from core import Files
from library.stigma.application import Anchor
from library.stigma.helper import kivyBuilder, animation
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'homesidecontent.kv')


class HomeSidecontent(Anchor):
    def __init__(self):
        super(HomeSidecontent, self).__init__()
        self.anchor_y = 'center'

    def showing(self):
        animation(self, ({'height' : 600, 'd': .2},))