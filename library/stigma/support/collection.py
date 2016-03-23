'''
Collection stigma
=================
This is used to collect any data to object and to make it more flexible.

:package :     library stigma
'''


class _SCollect(object):

    _collect = None
    _collect_obj = None


class CollectMap(_SCollect):
    def __init__(self, default= None, **kwargs):
        '''
        this is consttuctor of collection mapping class.
        '''
        super(CollectMap, self).__init__()

        self._collect_obj = type('lambdaobject', (object, ), {})()
        self._collect = kwargs

    def append(self, **kwargs):
        '''
        used to appending map dictionary
        '''
        self._collect.update(kwargs)
        return self

    def inject(self, key, value):
        '''
        used for inject some key into value.
        '''
        self._collect[key] = value
        return self

    def pop(self, what):
        '''
        used to remove some key with it's value.
        '''
        self._collect.pop(what)
        return self

    @property
    def show(self):
        '''
        used for showing about the collection result.
        '''
        return self._collect

    @property
    def transform(self):
        '''
        used for transorming the dictionary collection into object data.
        '''
        for k, v in self._collect.items():
            if isinstance(k, basestring):
                self._collect_obj.__setattr__(k, v)

        return self._collect_obj