'''
BEHAVIOR
========
Behavior module is used to manage your event behavior of your widget or layout,
in here you will managed "what the application should do".

:usage  : you need to create DIY function inside the class, say you want to create
          a trigger event for your widget.

.. note::
    the behavior class is a sub class from core behavior the class is abstract and
    had an abstract method called collection. you need to define that "collection"
    method right in the class, and after that you have to set that as property.
    because the core need that as property to sending into your model.

see "Behavior" documentation for more information.
'''
from core import Behavior
from library.stigma.support.collection import CollectMap
from library.stigma.helper import eventAttach, clocker


class Behavior(Behavior):

    def __init__(self):
        '''
        this is behavior class, in here I gonna write what behavior application need to do, like
        open game, serialization, visual, even dialogue.

        :return:
        '''
        super(Behavior, self).__init__()

        # In controller Game there's a custom method ( it's not abstract method ) it will collect the game
        # control needed from behavior method.

        self.controller.Game.collection(self.instanceDialogue, self.instanceVisualization,
                                        self.instanceEnding, self.modalOption)
        self.controller.Game.widget = {'background' : self.widget.GameImagebackground,
                                       'dialogue'   : self.widget.GameTextdialogue,
                                       'name'       : self.widget.GameTextname,
                                       'save'       : self.widget.GameButtonsave,
                                       'character'  : [self.widget.GameImagepersoneone,
                                                       self.widget.GameImagepersonetwo]}
        self.use_load = None
        self.savedata = []

    # -- START OF ANIMATION METHOD --
    def animation(self, what, instance=None, anime='showing', duration=0):
        '''

        :param what:
        :param instance:
        :param anime:
        :param duration:
        '''
        if isinstance(what, str) and instance is not None:
            if what == 'layout':
                instance = getattr(self.layout, instance)
            elif what == 'widget':
                instance = getattr(self.widget, instance)

            clocker(lambda dt: getattr(instance, anime)(), 'once', duration)

    def animationIntro(self):
        '''

        :return:
        '''
        self.layout.IntroLayout.opacity = 0

        self.animation('layout', 'IntroLayout', 'showing', .1)
        self.animation('layout', 'IntroLayout', 'fading', 2.5)

    def animationHomeUp(self):
        '''
        This is initial Home animation, it will show a little animation when the application
        started running in first time, or application back to home.

        :return:
        '''
        self.layout.HomeLayout.opacity        = 0
        self.layout.HomeSidecontent.height    = 0
        self.widget.HomeImagelogo.opacity     = 0
        self.layout.HomeButtonwrapper.opacity = 0

        self.animation('layout', 'HomeLayout'       , 'showing', .1)
        self.animation('layout', 'HomeSidecontent'  , 'showing', .2)
        self.animation('widget', 'HomeImagelogo'    , 'showing', .25)
        self.animation('layout', 'HomeButtonwrapper', 'showing', .33)

    def animationHomeDown(self):
        '''

        :return:
        '''
        self.animation('layout', 'HomeLayout', 'fading', .1)

    def animationGameUp(self):
        '''

        '''
        self.layout.GameLayout.opacity = 0

        self.animation('layout', 'GameLayout', 'showing', .1)

    def animationEndUp(self):
        '''

        '''
        self.layout.EndLayout.opacity = 0

        self.animation('layout', 'EndLayout' , 'showing', .2)

    def animationEndDown(self):
        '''

        '''
        self.animation('layout', 'EndWrapper', 'fading', .2)
        self.animation('layout', 'EndLayout' , 'fading', .5)

    # -- END OF ANIMATION METHOD --
    # -- START OF MODELING METHOD --
    def openCloseModel(self, open_what = None, parameter = None, close_what = None):
        '''

        :param falsing:
        :return:
        '''
        if open_what is not None:
            if close_what is not None and isinstance(close_what, list):
                for v in close_what:
                    getattr(self.model, v)(False)

            if parameter is not None:
                getattr(self.model, open_what)(True, parameter)
            else:
                getattr(self.model, open_what)(True)

    def openIntro(self):
        '''

        :return:
        '''
        self.animationIntro()
        clocker(lambda dt: self.openCloseModel('home', None, ['intro']), 'once', 3)

    def openGame(self, parameter=None):
        '''
        This is an event function used for open Game, when the game is open I need to reset any unnecessary
        model and the game model should be reseted because it's bug if the model is already instanced and
        it instanced again.

        :param parameter:
        :return:
        '''
        self.eventCloseModal('SerializePopup')
        self.animationHomeDown()
        clocker(lambda dt: self.openCloseModel('game', parameter, ['home', 'ending', 'game',]), 'once', .1)

    def openEndCloseGame(self, end):
        '''
        This is an function used to open the Ending of game.

        :param end:
        :return:
        '''
        clocker(lambda dt: self.openCloseModel('ending', end, ['game']), 'once', .1)

    def openHome(self, parameter = None):
        '''

        :return:
        '''
        if parameter == 'ending':
            self.animationEndDown()
            clocker(lambda dt: self.openCloseModel('home', None, ['ending']), 'once', .1)

        elif parameter == 'gaming':
            clocker(lambda dt: self.openCloseModel('home', None, ['game']), 'once', .1)

    # -- END OF MODELING METHOD --
    # -- START OF EVENT METHOD --
    def eventDialogue(self, background = None, character = None):
        '''
        this function is use to change the conversation game.

        :return:
        '''
        if background is not None or character is not None:
            self.instanceVisualization(background, character)

        current_part = self.widget.GameTextdialogue.part
        self.controller.Game.plot(current_part)

    def eventCloseModal(self, layout, model = None):
        '''
        This is a event option that used to close option serialization, option or anything
        based on parameter. it also to apart model function.

        :param layout:
        :param model:
        :return:
        '''
        if isinstance(layout, basestring):
            getattr(self.layout, layout).dismiss()

            if model is not None and isinstance(model, basestring):
                getattr(self.model, model)(False)

    # -- END OF EVENT METHOD --
    # -- START OF INSTANCE METHOD --
    def instanceDialogue(self, part, line, state = None):
        '''
        Same as below, is manage the dialogue between NPC and player in game, it also manage
        the option if player used to serialization or option.

        :param part:
        :param line:
        :param state:
        :return:
        '''
        if isinstance(part, basestring) and isinstance(line, int):
            if state == 'loadsave':
                self.eventCloseModal('SerializePopup', 'serialize')
            elif state == 'option':
                self.eventCloseModal('OptionPopup', 'option')

            self.widget.GameTextdialogue.part = [part, line]
            conversation = self.controller.Game.conversation(part, line)[0]
            self.controller.Game.dialog(conversation, [part, line])

    def instanceVisualization(self, background = None, who = None):
        '''
        This function is manange the behavior about visualization game, like character or
        background game in some state.

        :param background:
        :param who:
        :return:
        '''
        self.controller.Game.visual(background, who)

    def instanceEnding(self, ending):
        for k, v in ending.items():
            end_img = self.controller.Game.event(k, v)
        self.openEndCloseGame(end_img)

    # -- END OF INSTANCE METHOD --
    # -- START OF MODAL METHOD --
    def modalSerialization(self, serialization):
        '''
        This is an event to show serialization dialog like save or load data application.
        it used to save some state of application or load them to continue the state application.

        :param serialization:
        :return:
        '''
        self.model.serialize(serialization, self.controller.Serialize.list)
        self.layout.SerializePopup.open()

    def modalOption(self, option):
        '''
        This event function is used for showing option for application, say when you play the game
        in some state and there's a checkpoint for your option. it will show as your option.

        :param option:
        :return:
        '''
        option = self.controller.Game.option(option)
        self.model.option(option)
        self.layout.OptionPopup.open()

    def saveGame(self, slot):
        '''

        :param slot:
        :return:
        '''
        if slot is not None and isinstance(slot, int):
            key = 'save_%s' %slot
            data = {key : {}}

            data[key].update(self.widget.GameButtonsave.data)
            data[key].update(self.widget.GameButtonsave.graphic)

            self.controller.Serialize.save(slot=slot, write=data)

    @property
    def alias(self):
        '''
        this is an abstract method from core, you need to define it as function,
        and after that don't forget to declare it as property.

        :return :       the method you wanted.
        '''
        recole = CollectMap(animation              = self.animation,
                            animation_home_up      = self.animationHomeUp,
                            animation_game_up      = self.animationGameUp,
                            animation_end_up       = self.animationEndUp,
                            open_intro             = self.openIntro,
                            open_home              = eventAttach(self.openHome, 'on_press'),
                            event_dialogue         = self.eventDialogue,
                            touched_event_dialogue = eventAttach(self.eventDialogue, 'on_touch_down'),
                            open_game              = eventAttach(self.openGame, 'on_press'),
                            open_serialization     = eventAttach(self.modalSerialization, 'on_press'),
                            save_game              = eventAttach(self.saveGame, 'on_press'))
        return recole.transform