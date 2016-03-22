from core import Files
from library.stigma.application import Float
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'game', 'container.kv')


class GameContainer(Float):
    def __init__(self):
        super(GameContainer, self).__init__()