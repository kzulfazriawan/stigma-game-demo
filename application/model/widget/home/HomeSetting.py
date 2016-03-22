from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'setting.kv')


class HomeSetting(Button):
    def __init__(self):
        super(HomeSetting, self).__init__()
        self.text = 'Setting'