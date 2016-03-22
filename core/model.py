'''
CORE MODEL
==========
it's a core about model inheritance from Anchor in application core, this class
provide standard and anything for class model class in application.

:package :     core stigma
'''
from abc import abstractmethod, ABCMeta
from core.application import Anchor


class _Model(Anchor):
    '''
    model base class, for parent class model below. used to provide variable,
    object and type_data only for model needed.
    '''
    behavior = None


class Model(_Model):
    __metaclass__ = ABCMeta

    def __init__(self):
        '''
        Model class, you can check it from the documentation for more information

        .. log changed class::
            .. version 0.0.6::
                The name of abstract method for declare all it's function has been
                changed from "bundle" to "collection".
        '''
        super(Model, self).__init__()

    @abstractmethod
    def collection(self):
        '''
        an abstract method is used to collecting method model for application to build.
        '''
        pass