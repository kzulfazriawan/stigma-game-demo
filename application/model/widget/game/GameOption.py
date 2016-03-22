from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'Option.kv')


class GameOption(Button):
    def __init__(self):
        super(GameOption, self).__init__()