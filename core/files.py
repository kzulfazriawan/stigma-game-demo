'''
Files Core
==========

:module :
'''
import sys , imp, os


class _CFiles(object):
    '''
    this is files base class, is used for inheritance for Files.
    '''
    corepath = ''
    apppath  = ''
    confpath = ''
    libspath = ''
    rootpath = ''


class Files(_CFiles):
    def __init__(self, **kwargs):
        '''
        core class for filesystem configurations.

        :param kwargs:      dictionary path
        '''
        super(Files, self).__init__()

        self.require = None
        self.checker = False
        self.checkout = None

        # -- Core path is initialized since when I declared the class.
        self.rootpath = kwargs['root']
        self.corepath = kwargs['core']
        self.apppath = kwargs['apps']
        self.confpath = kwargs['conf']
        self.libspath = kwargs['libs']

    def _impoter(self, instance, substance):
        '''
        this private method used to import modules dynamically.

        :param instance:    pakcage modules
        :param substance:   modules class
        :return:            the module it self
        '''
        pathmod = os.path.join(instance, substance)

        try:
            return sys.modules[pathmod]
        except KeyError:
            pass

        try:
            fp, pathname, description = imp.find_module(pathmod)
            try:
                return imp.load_module(pathmod, fp, pathname, description)
            finally:
                if fp:
                    fp.close()

        except ImportError:
            sys.path.insert(0, os.path.join(self.rootpath, os.path.dirname(pathmod)))
            try:
                return __import__(os.path.basename(pathmod), globals(), locals(), [])

            except ImportError as Err:
                raise Err

    def getClass(self, modules, klass):
        '''
        this used to get class dynamically from some packages.

        :param modules:     the module files
        :param klass:       class wanted
        :return:            class object from module
        '''
        objmod = self._impoter(modules, klass)
        klass = getattr(objmod, klass)
        return klass()