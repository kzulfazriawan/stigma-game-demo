from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'quitgame.kv')


class HomeQuitgame(Button):
    def __init__(self):
        super(HomeQuitgame, self).__init__()
        self.text = 'Quit game'