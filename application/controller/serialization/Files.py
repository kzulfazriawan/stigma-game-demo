import os
from stat import S_ISREG
from abc import ABCMeta
from core import Files


class Directory(object):
    __metaclass__ = ABCMeta
    directory = os.path.join(Files.rootpath, 'saves')

    def listFiles(self):
        '''
        this is a function to show the data from directory save, so basically
        the directory save will load any file inside it and return it as directory

        :return :      data directory files.
        '''
        if os.path.exists(self.directory):
            files = {}

            for k, v in enumerate(os.listdir(self.directory)):
                save = os.path.join(self.directory, v)
                mode  = os.stat(save).st_mode

                if S_ISREG(mode):
                    files.update({int(v.strip('.json')) : save})

            return files

    def dumpFiles(self, what, name):
        '''


        :param  :what:
        :param  :name:
        :return :
        '''
        if os.path.exists(self.directory):
            files = os.path.join(self.directory, name)

            try:
                open_file = open(files, 'w')
                open_file.write(what)
            except IOError as E:
                raise E
            else:
                open_file.close()