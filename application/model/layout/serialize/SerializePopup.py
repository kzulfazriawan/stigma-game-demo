from core import Files
from library.stigma.helper import kivyBuilder
from library.stigma.application import Popup
kivyBuilder(Files.apppath, 'model', 'builder', 'serialize', 'serializepopup.kv')


class SerializePopup(Popup):
    def __init__(self):
        super(SerializePopup, self).__init__()
        self.title = "Save / Load"