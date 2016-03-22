from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'wrapper.kv')


class OptionWrapper(Box):
    def __init__(self):
        super(OptionWrapper, self).__init__()
        self.orientation = 'vertical'