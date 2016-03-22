from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'buttontri.kv')


class OptionButtontri(Button):
    def __init__(self):
        super(OptionButtontri, self).__init__()
        self.params = None