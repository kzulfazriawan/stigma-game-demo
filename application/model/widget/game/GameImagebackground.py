from core import Files
from library.stigma.application import Image
from library.stigma.helper import kivyBuilder, animation, clocker
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gameimagebackground.kv')


class GameImagebackground(Image):
    def __init__(self):
        super(GameImagebackground, self).__init__()

    def focus(self, source):
        if isinstance(source, str):
            animation(self, ({'opacity': 0, 'd': .1},))
            clocker(lambda dt : animation(self, ({'opacity': 1, 'd': .3},)), 'once', .12)
            clocker(lambda dt : self._changing(source), 'once', .12)

    def _changing(self, source):
        self.source = source