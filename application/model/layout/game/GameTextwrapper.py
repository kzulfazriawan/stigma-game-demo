from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gametextwrapper.kv')


class GameTextwrapper(Box):
    def __init__(self):
        super(GameTextwrapper, self).__init__()