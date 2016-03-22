from library.stigma.application import Float

from Model import Model
from Alias import Alias
from Behavior import Behavior


class Application(Float):
    def __init__(self):
        super(Application, self).__init__()

        model = Model()
        behavior = Behavior()

        model.layout , model.widget = (Alias.layout, Alias.widget)
        behavior.layout, behavior.widget = (Alias.layout, Alias.widget)
        behavior.model , model.behavior = (model, behavior.collection)

        self.gathering(model.collection)
        self.adding