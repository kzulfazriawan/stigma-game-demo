from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'newgame.kv')


class HomeNewgame(Button):
    def __init__(self):
        super(HomeNewgame, self).__init__()
        self.text   = 'New game'
        self.params = None