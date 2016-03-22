from application.controller.resources.Background import Background


class Event(object):
    background = Background()

    def ending(self, ending):
        if ending == 'good':
            return self.background.ending
        elif ending == 'bad':
            return self.background.badending
