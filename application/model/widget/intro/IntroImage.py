from core import Files
from library.stigma.application import Image
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder','intro', 'introimage.kv')


class IntroImage(Image):
    def __init__(self):
        super(IntroImage, self).__init__()