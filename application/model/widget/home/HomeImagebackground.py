from core import Files
from library.stigma.application import Image
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'imagebackground.kv')


class HomeImagebackground(Image):
    def __init__(self):
        super(HomeImagebackground, self).__init__()