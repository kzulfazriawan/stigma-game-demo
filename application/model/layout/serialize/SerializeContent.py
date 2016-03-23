from core import Files
from library.stigma.application import Box
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'serialize', 'serializecontent.kv')


class SerializeContent(Box):
    def __init__(self):
        super(SerializeContent, self).__init__()