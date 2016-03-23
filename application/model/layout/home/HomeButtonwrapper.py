from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder, animation
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'homebuttonwrapper.kv')


class HomeButtonwrapper(Box):
    def __init__(self):
        super(HomeButtonwrapper, self).__init__()

    def showing(self):
        animation(self, ({'opacity': 1, 'd': .5},))