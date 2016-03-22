'''
CORE WINDOW
================
it's a core window use in globally needed, in this module provide standard,
variable, object and anything the window needed.

:package  :         core stigma
'''
from kivy.config import Config


class _CWindows(object):
    '''
    this is windows base class, is used for inheritance for Window usage.
    '''
    config = Config


class Windows(_CWindows):

    def __init__(self, **kwargs):
        '''
        this is window class used for manage window interface for application.

        :param kwargs:
        '''
        super(Windows, self).__init__()
        self.app = kwargs['app']

    @property
    def setWindow(self):
        '''
        a method will set window based on configuration.

        :return:        variable configuration window
        '''
        for k, v in self.app.items():
            if isinstance(v, dict):
                for a, z in v.items():
                    self.config.set(k, a, z)

        return self.config

    def getWindow(self, info):
        '''
        a method will show information about window configuration.

        :param info:    string key variable configuration
        :return:        information configuration
        '''
        return self.app[info]