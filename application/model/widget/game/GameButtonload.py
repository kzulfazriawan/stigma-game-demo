from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gamebuttonload.kv')


class GameButtonload(Button):
    def __init__(self):
        super(GameButtonload, self).__init__()
        self.text = 'Load'
        self.params = 'load'