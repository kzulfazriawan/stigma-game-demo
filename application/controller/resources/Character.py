import os
from core import Files


class Character(object):
    '''

    '''
    stigma = {
        'usual': os.path.join(format(Files.rootpath), 'assets', 'image', 'character', 'stigma', 'usual.png'),
        'talk': os.path.join(format(Files.rootpath), 'assets', 'image', 'character', 'stigma', 'talk.png'),
        'smile': os.path.join(format(Files.rootpath), 'assets', 'image', 'character', 'stigma', 'smile.png'),
        'shy': os.path.join(format(Files.rootpath), 'assets', 'image', 'character', 'stigma', 'shy.png')
    }
    kzul = {
        'usual' : '{}/assets/image/character/kzul/usual.png'.format(Files.rootpath),
        'talk'  : '{}/assets/image/character/kzul/talk.png'.format(Files.rootpath),
        'smile' : '{}/assets/image/character/kzul/smile.png'.format(Files.rootpath),
    }
    character = {
        'clear' : '{}/assets/image/character/clear.png'.format(Files.rootpath),
    }
