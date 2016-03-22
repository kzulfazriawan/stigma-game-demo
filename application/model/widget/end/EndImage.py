from core import Files
from library.stigma.application import Image
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'end', 'imagebackground.kv')


class EndImage(Image):
    def __init__(self):
        super(EndImage, self).__init__()