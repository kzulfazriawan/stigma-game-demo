from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'buttonone.kv')


class OptionButtonone(Button):
    def __init__(self):
        super(OptionButtonone, self).__init__()
        self.params = None