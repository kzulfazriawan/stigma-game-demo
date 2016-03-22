from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'overlay.kv')


class OptionOverlay(Box):
    def __init__(self):
        super(OptionOverlay, self).__init__()