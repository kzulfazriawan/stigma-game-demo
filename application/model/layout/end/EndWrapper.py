from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder, animation
kivyBuilder(Files.apppath, 'model', 'builder', 'end', 'endwrapper.kv')


class EndWrapper(Box):
    def __init__(self):
        super(EndWrapper, self).__init__()

    def showing(self):
       animation(self, ({'opacity' : 1, 'd': .2},))

    def fading(self):
       animation(self, ({'opacity' : 1, 'd': .2},))