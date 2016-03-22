from core import Files
from library.stigma.application import Label
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gametextdialogue.kv')


class GameTextdialogue(Label):
    def __init__(self):
        super(GameTextdialogue, self).__init__()
        self.state        = None
        self.save         = None
        self.params       = None
        self.part         = None
        self.touch_action = 1