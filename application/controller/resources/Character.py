from core import Files


class Character(object):
    '''

    '''
    # TODO : di format pake join path biar path support diwindows.
    stigma = {
        'usual' : '{}/assets/image/character/stigma/usual.png'.format(Files.rootpath),
        'talk'  : '{}/assets/image/character/stigma/talk.png'.format(Files.rootpath),
        'shy'   : '{}/assets/image/character/stigma/shy.png'.format(Files.rootpath),
        'smile' : '{}/assets/image/character/stigma/smile.png'.format(Files.rootpath),
    }
    teacher = {
        'usual' : '{}/assets/image/character/kzul/usual.png'.format(Files.rootpath),
        'talk'  : '{}/assets/image/character/kzul/talk.png'.format(Files.rootpath),
        'smile' : '{}/assets/image/character/kzul/usual.png'.format(Files.rootpath),
    }
    character = {
        'clear' : '{}/assets/image/character/clear.png'.format(Files.rootpath),
    }