from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'end', 'endbuttonexit.kv')


class EndButtonexit(Button):
    def __init__(self):
        super(EndButtonexit, self).__init__()
        self.text = 'Back to Home'
        self.params = 'ending'