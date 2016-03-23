'''
MODEL
=====
in this module you can set your layout, widget, controller and behaviour that you
already designed into any kind of things.

:usage  : same as behavior, but the difference is you manage "What the application
          looks like"

.. note::
    the model class is a sub class from core model, same as behavior it has abstract
    method called "collection", but the difference you can't define the return with
    you wanted. you have to set the return as a list or tuple.

see "Model" documentation for more information.
'''
from core import Model
from library.stigma.support.collection import CollectMap


class Model(Model):

    def __init__(self):
        '''
        A model class, in here I gonna structurized my layout and widget for game functionality.
        there's home, game, option, ending and serialize model layout.
        '''
        super(Model, self).__init__()
        self.option_bind_store    = []
        self.option_widget_store  = None
        self.serialize_bind_store = None

    def intro(self, assemble=True):
        '''
        Intro display, it will displayed intro application when application first time started

        :param assemble:    boolean assemble model
        :return:            widget of IntroLayout
        '''
        self.layout.IntroLayout.gathering([self.widget.IntroImage])

        # -- when the model set as assemble True it will adding some layout
        # -- and widget, if not then remove it.
        if assemble == True:
            self.behavior.open_intro()
            self.layout.IntroLayout.adding
        else:
            self.layout.IntroLayout.removing

        return self.layout.IntroLayout

    def home(self, assemble=True):
        '''
        home display, like homepage application it appear on first time or when the game ended.
        '''
        self.layout.HomeImagewrapper.gathering([self.widget.HomeImagebackground,
                                                self.widget.HomeImagelogo])
        self.layout.HomeButtonwrapper.gathering([self.widget.HomeNewgame,
                                                 self.widget.HomeLoadgame,
                                                 self.widget.HomeQuitgame])
        self.layout.HomeSidecontent.gathering([self.layout.HomeButtonwrapper])
        self.layout.HomeLayout.gathering([self.layout.HomeImagewrapper,
                                          self.layout.HomeSidecontent])
    
        if assemble == True:
            # -- when the assemble set True, all widget will binding the event
            # -- from behavior.
            self.widget.HomeNewgame.bound(event='on_press' , bind=self.behavior.open_game)
            self.widget.HomeLoadgame.bound(event='on_press', bind=self.behavior.open_serialization)

            self.behavior.animation_home_up()

            self.layout.HomeImagewrapper.adding
            self.layout.HomeButtonwrapper.adding
            self.layout.HomeSidecontent.adding
            self.layout.HomeLayout.adding
        else:
            self.layout.HomeImagewrapper.removing
            self.layout.HomeButtonwrapper.removing
            self.layout.HomeSidecontent.removing
            self.layout.HomeLayout.removing

        return self.layout.HomeLayout

    def game(self, assemble=True, parameter = None):
        '''
        Model game play
        '''
        self.layout.GameContainer.gathering([self.widget.GameImagebackground,
                                             self.widget.GameImagepersoneone,
                                             self.widget.GameImagepersonetwo])
        self.layout.GameButtonwrapper.gathering([self.widget.GameButtonsave,
                                                 self.widget.GameButtonload,
                                                 self.widget.GameButtontitle])
        self.layout.GameTextwrapper.gathering([self.widget.GameTextname,
                                               self.widget.GameTextdialogue])
        self.layout.GameFooter.gathering([self.layout.GameTextwrapper,
                                          self.layout.GameButtonwrapper])
        self.layout.GameLayout.gathering([self.layout.GameContainer,
                                          self.layout.GameFooter])

        if assemble == True:
            # -- if state from text dialog is empty, it means game is not
            # -- instance yet, it means the application is just running.
            if self.widget.GameTextdialogue.state is None:
                if parameter is not None and (isinstance(parameter, list) or isinstance(parameter, tuple)):
                    background, part, character, line, state = parameter
                else:
                    part       = 'intro'
                    line       = -1
                    background = None
                    character  = None

                self.widget.GameImagepersoneone.reset()
                self.widget.GameImagepersonetwo.reset()

                self.widget.GameTextdialogue.part = [part, line]
                self.behavior.event_dialogue(background, character)

            self.widget.GameButtonsave.bound(event='on_press', bind=self.behavior.open_serialization)
            self.widget.GameButtonload.bound(event='on_press', bind=self.behavior.open_serialization)
            self.widget.GameButtontitle.bound(event='on_press', bind=self.behavior.open_home)
            self.widget.GameTextdialogue.bound(event='on_touch_down', bind=self.behavior.touched_event_dialogue)

            self.behavior.animation_game_up()

            self.layout.GameContainer.adding
            self.layout.GameButtonwrapper.adding
            self.layout.GameTextwrapper.adding
            self.layout.GameFooter.adding
            self.layout.GameLayout.adding
        else:
            self.layout.GameContainer.removing
            self.layout.GameButtonwrapper.removing
            self.layout.GameTextwrapper.removing
            self.layout.GameFooter.removing
            self.layout.GameLayout.removing

        return self.layout.GameLayout

    def ending(self, assemble=True, end = None):
        '''
        ending of game
        '''
        self.layout.EndContainer.gathering([self.widget.EndImage])
        self.layout.EndWrapper.gathering([self.widget.EndButtonexit,
                                          self.widget.EndButtonload])
        self.layout.EndLayout.gathering([self.layout.EndContainer,
                                         self.layout.EndWrapper])

        if assemble == True:
            if end is not None:
                self.widget.EndImage.source = end

            self.widget.EndButtonexit.bound(event='on_press', bind=self.behavior.open_home)
            self.widget.EndButtonload.bound(event='on_press', bind=self.behavior.open_serialization)

            # -- instance the behavior animation ending up, to show up ending
            # -- with animation.
            self.behavior.animation_end_up()

            self.layout.EndContainer.adding
            self.layout.EndWrapper.adding
            self.layout.EndLayout.adding

        else:
            self.layout.EndContainer.removing
            self.layout.EndWrapper.removing
            self.layout.EndLayout.removing

        return self.layout.EndLayout

    def option(self, opt=None):
        '''
        this is function when the scenario reach the option route for game application.
        here the widget had 4 default button, it used to store the event for option game.
        '''
        if opt is not None and isinstance(opt, dict):

            option_modal, option_binder = ([], [])
            button_modal = [self.widget.OptionButtonone,
                            self.widget.OptionButtontwo,
                            self.widget.OptionButtontri,
                            self.widget.OptionButtonfor]
            i = 0

            for k, v in opt.items():
                button_modal[i].text = str(k).replace('_', ' ').capitalize()
                option_binder.append(v)
                option_modal.append(button_modal[i])
                i += 1

            if self.option_widget_store is not None and isinstance(self.option_widget_store, list):
                self.layout.OptionOption.gathering(self.option_widget_store)
                self.layout.OptionOption.removing

            self.layout.OptionOption.gathering(option_modal)
            self.layout.OptionWrapper.gathering([self.layout.OptionOption])
            self.layout.OptionContainer.gathering([self.layout.OptionWrapper])
            self.layout.OptionPopup.gathering([self.layout.OptionContainer])

            for k, v in enumerate(option_binder):
                if len(self.option_bind_store) > 1:
                    try:
                        option_modal[k].bound(event='on_press', bind=v, unbind=self.option_bind_store[k])
                        self.option_bind_store[k] = v

                    except IndexError:
                        option_modal[k].bound(event='on_press', bind=v)
                        self.option_bind_store.append(v)
                else:
                    option_modal[k].bound(event='on_press', bind=v)
                    self.option_bind_store.append(v)

            self.option_widget_store = option_modal

            self.layout.OptionOption.removing
            self.layout.OptionWrapper.removing
            self.layout.OptionContainer.removing
            self.layout.OptionPopup.removing

            self.layout.OptionOption.adding
            self.layout.OptionWrapper.adding
            self.layout.OptionContainer.adding
            self.layout.OptionPopup.adding

        return self.layout.OptionPopup

    def serialize(self, option = None, savedata = []):
        '''
        this is model for dialog serialization like load or save state in application game.
        '''
        if option is not None:
            list_button = [
                self.widget.SerializeButtonone,
                self.widget.SerializeButtontwo,
                self.widget.SerializeButtontri,
                self.widget.SerializeButtonfor
            ]

            unbinder = {}

            for k in range(len(list_button)):
                if option == 'load':
                    try:
                        index, part, line, background, character = savedata[k]
                        list_button[index].params = (background, part , character, int(line) - 1, None)
                        if self.serialize_bind_store is not None:
                            list_button[index].bound(event='on_press', bind=self.behavior.open_game, unbind=self.serialize_bind_store[index])
                        else:
                            list_button[index].bound(event='on_press', bind=self.behavior.open_game)

                        unbinder.update({index : self.behavior.open_game})
                    except IndexError:
                        pass

                if option == 'save':
                    try:
                        list_button[k].params = k
                        if self.serialize_bind_store is not None:
                            list_button[k].bound(event='on_press', bind=self.behavior.save_game, unbind=self.serialize_bind_store[k])
                        else:
                            list_button[k].bound(event='on_press', bind=self.behavior.save_game)

                    except KeyError:
                        pass

                    unbinder.update({k : self.behavior.open_game})

            self.serialize_bind_store = unbinder

            self.layout.SerializeContent.gathering(list_button)
            self.layout.SerializePopup.gathering([self.layout.SerializeContent])

            self.layout.SerializeContent.removing
            self.layout.SerializePopup.removing

            self.layout.SerializeContent.adding
            self.layout.SerializePopup.adding

        return self.layout.SerializePopup

    @property
    def layer(self):
        '''
        The alias I turned into property because it had no parameter needed inside.
        '''
        return [self.ending(False), self.game(False), self.home(False), self.intro(True)]