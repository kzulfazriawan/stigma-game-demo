from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'buttontwo.kv')


class OptionButtontwo(Button):
    def __init__(self):
        super(OptionButtontwo, self).__init__()
        self.params = None