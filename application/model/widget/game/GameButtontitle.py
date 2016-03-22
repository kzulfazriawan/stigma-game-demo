from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gamebuttonoption.kv')


class GameButtontitle(Button):
    def __init__(self):
        super(GameButtontitle, self).__init__()
        self.text = 'Title'
        self.params = 'gaming'