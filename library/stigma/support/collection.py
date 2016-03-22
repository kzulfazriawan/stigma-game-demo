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

        :param default:
        :param kwargs:
        '''
        super(CollectMap, self).__init__()

        self._collect_obj = type('lambdaobject', (object, ), {})()
        self._collect = kwargs

    def append(self, **kwargs):
        '''
        used to appending map dictionary

        :param kwargs:      dictionary to append
        :return:            self class
        '''
        self._collect.update(kwargs)
        return self

    def inject(self, key, value):
        '''
        used for inject some key into value.

        :param key:         the key
        :param value:       value you wanted
        :return:            self class
        '''
        self._collect[key] = value
        return self

    def pop(self, what):
        '''
        used to remove some key with it's value.

        :param what:        the key
        :return:            self class
        '''
        self._collect.pop(what)
        return self

    @property
    def show(self):
        '''
        used for showing about the collection result.

        :return:            collection result
        '''
        return self._collect

    @property
    def transform(self):
        '''
        used for transorming the dictionary collection into object data.

        :return:            collection object
        '''
        for k, v in self._collect.items():
            if isinstance(k, basestring):
                self._collect_obj.__setattr__(k, v)

        return self._collect_obj