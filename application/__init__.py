from kivy.app import App

from library.stigma.application import Float

from Alias import Alias
from Model import Model
from Behavior import Behavior


class Application(Float):
    def __init__(self):
        '''
        Application class used for merging between model and behavior.
        '''
        super(Application, self).__init__()

        model = Model()
        behavior = Behavior()

        behavior.model , model.behavior = (model, behavior.alias)

        self.gathering(model.layer)
        self.adding


class MainApplication(App):
    def __init__(self):
        '''
        Main Application or we call it Base Window Kivy.
        '''
        super(MainApplication, self).__init__()
        self._application = Application()

    def build(self):
        '''
        Everything we need to build constructed here.
        '''

        return self._application
