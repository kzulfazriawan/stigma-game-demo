from library.stigma.application import Button


class HomeLoadgame(Button):
    def __init__(self):
        super(HomeLoadgame, self).__init__()
        self.text   = 'Load game'
        self.params = 'load'