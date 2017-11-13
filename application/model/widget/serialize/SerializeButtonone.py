from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'Buttonone.kv')


class SerializeButtonone(Button):
    def __init__(self):
        super(SerializeButtonone, self).__init__()
        self.value  = '0'
        self.text  = 'SLOT 1'
        self.data   = None
        self.params = int(self.value)