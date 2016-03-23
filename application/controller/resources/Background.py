import os
from core import Files


class Background(object):
    '''
    This is class used to storage the background
    '''
    meet_stigma  = os.path.join(Files.rootpath, 'assets', 'image', 'background', 'meet_stigma.png')
    geo          = os.path.join(Files.rootpath, 'assets', 'image', 'background', 'geo.png')
    ending       = os.path.join(Files.rootpath, 'assets', 'image', 'background', 'goodend.png')
    badending    = os.path.join(Files.rootpath, 'assets', 'image', 'background', 'badend.png')
