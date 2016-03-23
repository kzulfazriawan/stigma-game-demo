from abc import ABCMeta
from application.controller.game.Graphics import Graphics
from application.controller.game.Scenario import Scenario
from application.controller.game.Event import Event


class State(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.graphics = Graphics()
        self.scenario = Scenario()
        self.events   = Event()

    def background(self, where, widget):
        '''
        here's state will do as the command say for change the graphics background as the scenario
        says.
        '''
        return self.graphics.background(where, widget)

    def character(self, character, widget):
        '''
        same as above, but this method is used to change the character.
        '''
        return self.graphics.character(character, widget)

    def conversation(self, part, line):
        '''
        same as before, but this time it changed the conversation from the scenario.
        '''
        return self.scenario.conversation(part, line)

    def dialogue(self, conversation, widget, state):
        '''
        when the conversation from game is changed as the event command, it also changed from the widget
        that game already passed.
        '''
        if isinstance(conversation, dict) and (isinstance(widget, list) or isinstance(widget, tuple)):
            name, dialog, save = widget
            data = {}
            key  = ['part' , 'line']

            for k, v in conversation.items():
                if k != 'self':
                    name.text = k
                else:
                    name.text = ''

                dialog.text = v

                for x, y in enumerate(state):
                    data.update({key[x] : y})

                save.data = data

    def event(self, call, parameter):
        if isinstance(call, str):
            return getattr(self.events, call)(parameter)

    def modal(self, option, function):
        '''
        when the scenario reach some event when the option need to be showed, this method will provide the
        option for the application game.
        '''
        return self.scenario.option(option, function)