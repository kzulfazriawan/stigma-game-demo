from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'Buttontwo.kv')


class SerializeButtonfor(Button):
    def __init__(self):
        super(SerializeButtonfor, self).__init__()
        self.value  = '3'
        self.text  = 'SLOT 4'
        self.data   = None
        self.params = int(self.value)