from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'buttonfor.kv')


class OptionButtonfor(Button):
    def __init__(self):
        super(OptionButtonfor, self).__init__()
        self.params = None