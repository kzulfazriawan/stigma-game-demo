from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'loadgame.kv')


class HomeLoadgame(Button):
    def __init__(self):
        super(HomeLoadgame, self).__init__()
        self.text   = 'Load game'
        self.params = 'load'