from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'Popup.kv')


class GamePopup(Box):
    def __init__(self):
        super(GamePopup, self).__init__()