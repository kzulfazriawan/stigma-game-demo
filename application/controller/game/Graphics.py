from application.controller.resources.Background import Background
from application.controller.resources.Character import Character


class Graphics(object):
    _character  = Character()
    _background = Background()

    _environ_width    = 800
    _sum_dialog_store = 0

    def background(self, where, widget):
        '''
        function that would provide the widget with source image.
        '''
        if where is not None and isinstance(widget, object):
            widget.focus(getattr(self._background, where))

    def character(self, who, widget):
        '''
        function used to calculated, show up, and reset character.
        '''
        if isinstance(who, dict) and (isinstance(widget, list) or isinstance(widget, tuple)):
            i              = 0
            sum_character  = len(who)

            center  = self._environ_width / 2
            y_axis  = 0
            x_part  = (center / sum_character) - 150
            character = ''

            if self._sum_dialog_store > sum_character:
                widget[1].reset()

            for k, v in who.items():
                if sum_character > 1:
                    x_axis = (center * i) + x_part

                else:
                    x_axis = x_part

                if k != 'character':
                    expression = v[0]
                    character  = getattr(self._character, k)
                    character  = character[expression]
                    position   = (x_axis, y_axis)

                    widget[i].focus(character, position)

                    try:
                        animation = v[1]
                        getattr(widget[i], animation)(True)
                    except IndexError:
                        pass

                else:
                    if v == 'reset':
                        for i in range(sum_character):
                            widget[i].reset()

                i += 1

            self._sum_dialog_store = sum_character