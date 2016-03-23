'''
CORE APPLICATION
================
it's a core application use in globally needed, in this module provide standard,
variable, object and anything the application needed.

:package  :         core stigma
'''
import os


class _CApplication(object):
    '''
    this is application base class, is used for inheritance for Application or Alias.
    '''
    layout = type('lambdaobject', (object, ), {})()
    widget = type('lambdaobject', (object, ), {})()
    controller = type('lambdaobject', (object, ), {})()


def _separating(data):
    '''
    this is just a simple application used for separate the alias widget with it's path.
    '''
    if isinstance(data, basestring):
        data = data.split('@')
        if len(data) <= 2:
            return data


class Alias(_CApplication):
    def __init__(self, apppath, getClass=object):
        '''
        this is Alias class, is used to aliasing object into method that ease the user
        to define object.
        '''
        super(Alias, self).__init__()

        if os.path.isdir(apppath):
            self.modelpath = os.path.join(apppath, 'model')
            self.controlpath = os.path.join(apppath, 'controller')
            self.importer = getClass

    def setInstance(self, place, key, instances):
        '''
        this is an method used for instancing the object into method in lambda object.
        '''
        instances = _separating(instances)
        if isinstance(instances, list) and isinstance(key, basestring):
            if place is 'layout':
                setattr(self.layout, key,
                        self.importer(os.path.join(self.modelpath, place, instances[1]), instances[0]))
            elif place is 'widget':
                setattr(self.widget, key,
                        self.importer(os.path.join(self.modelpath, place, instances[1]), instances[0]))
            elif place is 'controller':
                setattr(self.controller, key,
                        self.importer(os.path.join(os.path.dirname(self.controlpath), place, instances[1]),
                                      instances[0]))
            return self

    def setAll(self, setdict):
        '''
        this is an method to set the instance in one way, if you gonna use set instance instead
        setAll it's ok.
        '''
        if isinstance(setdict, dict) and setdict is not None:
            for k, v in setdict.items():
                if isinstance(v, tuple) or isinstance(v, list):
                    for x in v:
                        self.setInstance(k, x[0], x[1])


class Anchor(_CApplication):
    def __init__(self):
        '''
        this is an anchor class,
        '''
        super(Anchor, self).__init__()
