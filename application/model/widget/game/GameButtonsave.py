from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gamebuttonsave.kv')


class GameButtonsave(Button):
    def __init__(self):
        super(GameButtonsave, self).__init__()
        self.text    = 'Save'
        self.value   = 'save'
        self.data    = None
        self.graphic = {'background' : 'None', 'character' : 'None'}
        self.params  = 'save'