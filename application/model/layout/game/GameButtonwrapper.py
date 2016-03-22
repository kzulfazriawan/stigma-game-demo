from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gamebuttonwrapper.kv')


class GameButtonwrapper(Box):
    def __init__(self):
        super(GameButtonwrapper, self).__init__() 