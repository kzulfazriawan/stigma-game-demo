from core import Files
from library.stigma.helper import kivyBuilder
from library.stigma.application import Popup
kivyBuilder(Files.apppath, 'model', 'builder', 'option', 'optionpopup.kv')


class OptionPopup(Popup):
    def __init__(self):
        super(OptionPopup, self).__init__()