from core import Files
from library.stigma.application import Label
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'gametextname.kv')


class GameTextname(Label):
    def __init__(self):
        super(GameTextname, self).__init__()
        self.text   = ''
        self.params = None