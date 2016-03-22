from core import Files
from library.stigma.application import Image
from library.stigma.helper import kivyBuilder, animation
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'homeimagelogo.kv')


class HomeImagelogo(Image):
    def __init__(self):
        super(HomeImagelogo, self).__init__()

    def showing(self):
        animation(self, ({'opacity': 1, 'd': .5},))