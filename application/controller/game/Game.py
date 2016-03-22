from application.controller.game.State import State
from library.stigma.helper import clocker


class Game(State):

    def __init__(self):
        '''
        this is game class that will handle some control in game application like dialogue, option,
        plot and even visual.

        :return:
        '''
        super(Game, self).__init__()

        # -- here's the behavior function that I collected from it to manage this class Game.
        # -- which behavior game should use.
        self._instance_dialogue = None
        self._instance_visual   = None
        self._option_show       = None
        self.widget             = {}
        self.sasdfa = []

    def collection(self, instanceDialogue, instanceVisual, instanceEnding, optionShow):
        '''
        This is collection function, it just a custom method that I created to handle the method
        from behavior class.

        :param instanceDialogue:
        :param instanceVisual:
        :param optionShow:
        :return:
        '''
        self._instance_dialogue = instanceDialogue
        self._instance_visual   = instanceVisual
        self._instance_ending   = instanceEnding
        self._option_show       = optionShow

        return self

    def dialog(self, conversation, state):
        '''
        this is override function dialog I created to passing some parameter into abstract class from state.

        :param conversation:
        :param state:
        :return:
        '''
        return self.dialogue(conversation, (self.widget['name'] , self.widget['dialogue'], self.widget['save']), state)

    def plot(self, current_state=None, modalize = None):
        '''
        this is a function when conversation in game is played based on scenario that I already
        create before.

        :param  :       list or tuple current state of game conversation
        '''
        if current_state is not None and (isinstance(current_state, list) or isinstance(current_state, tuple)):
            part, line = current_state
            present_scenario = self.conversation(part, line + 1)

            if isinstance(present_scenario, list) or isinstance(present_scenario, tuple):
                dialogue = present_scenario[0]
                try:
                    character = present_scenario[1]
                except IndexError:
                    character = None

                try:
                    background = present_scenario[2]
                except IndexError:
                    background = None

                self._instance_dialogue(part, line + 1, modalize)
                self._instance_visual(background, character)

            elif isinstance(present_scenario, basestring):
                self._option_show(present_scenario)

            elif isinstance(present_scenario, dict):
                self._instance_ending(present_scenario)

    def visual(self, background = None, character = None):
        '''
        This is a state function for visual stating in game, say when the scenario reach some event
        with background or character. it will do change the graphics as scenario write it.

        :param  :background:
        :param  :character:
        '''

        if background is not None and isinstance(background, basestring):
            self.background(background, self.widget['background'])
            self.widget['save'].graphic['background'] = background

        if character is not None and isinstance(character, dict):
            self.character(character, self.widget['character'])
            self.widget['save'].graphic['character'] = {}

            for k, v in character.items():
                self.widget['save'].graphic['character'].update({k : list(v)})

    def option(self, option):
        '''
        This is override function, it passing the class about the isntance dialogue method from behavior

        :param option:
        :return:
        '''
        return self.modal(option, self.plot)