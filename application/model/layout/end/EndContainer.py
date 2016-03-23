from core import Files
from library.stigma.application import Float
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'end', 'optioncontainer.kv')


class EndContainer(Float):
    def __init__(self):
        super(EndContainer, self).__init__()