from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'end', 'endbuttonload.kv')


class EndButtonload(Button):
    def __init__(self):
        super(EndButtonload, self).__init__()
        self.text = 'Load game'
        self.params = 'load'