from core import Files
from library.stigma.application import Anchor
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'Container.kv')


class OptionContainer(Anchor):
    def __init__(self):
        super(OptionContainer, self).__init__()