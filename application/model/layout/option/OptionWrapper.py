from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'optionwrapper.kv')


class OptionWrapper(Box):
    def __init__(self):
        super(OptionWrapper, self).__init__()
        self.orientation = 'vertical'