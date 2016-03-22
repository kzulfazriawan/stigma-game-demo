from core import Files
from library.stigma.application import Float
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'home', 'imagewrapper.kv')


class HomeImagewrapper(Float):
    def __init__(self):
        super(HomeImagewrapper, self).__init__()