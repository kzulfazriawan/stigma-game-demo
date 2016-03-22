from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gamefooter.kv')


class GameFooter(Box):
    def __init__(self):
        super(GameFooter, self).__init__()