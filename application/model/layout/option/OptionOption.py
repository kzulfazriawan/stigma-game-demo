from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'optionoption.kv')


class OptionOption(Box):
    def __init__(self):
        super(OptionOption, self).__init__()
        self.option = 0