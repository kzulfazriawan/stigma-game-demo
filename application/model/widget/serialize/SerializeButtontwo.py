from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'Buttontwo.kv')


class SerializeButtontwo(Button):
    def __init__(self):
        super(SerializeButtontwo, self).__init__()
        self.value  = '1'
        self.data   = None
        self.params = int(self.value)