'''
Factory stigma
==============
This is stigma factory application, in here the necessary method build for application
like bound, gathering, adding and even removing.

:package :     library stigma
'''


class ApplicationFactory(object):
    def __init__(self, baseclass=object):
        self.baseclass = baseclass

    @property
    def factoryWidget(self):
        '''
        Widget factory class.
        '''
        if isinstance(self.baseclass, object) and self.baseclass is not None:
            class SWidget(self.baseclass):
                _behaviour = []

                def bound(self, **kwargs):
                    '''
                    this function is used to bind any event for the widget it self.
                    '''
                    event = kwargs['event']

                    if isinstance(event, str):
                        try:
                            # -- some widget has problem with binding event, if the widget had bound event
                            # -- inside and try to replace it with another event it didn't works. so you
                            # -- must unbind the event before you attach the other one.
                            unbind = {event : kwargs['unbind']}
                            self.unbind(**unbind)
                        except KeyError:
                            pass

                        bind = {event : kwargs['bind']}
                        if bind is not None:
                            try:
                                self.bind(**bind)
                            except TypeError as E:
                                raise E

                        return self

            return SWidget

    @property
    def factoryInput(self):
        '''
        Factory Input, this factory is still a widget factory.
        '''
        if isinstance(self.baseclass, object) and self.baseclass is not None:
            class SInput(self.factoryWidget):
                _text_placeholder = ''

                def _placeholder(self, instance, value):
                    '''
                    Whoops ! this is event function, what the hell is it doing here !
                    well, since it's input factory class it would be better if input has
                    this feature.
                    '''
                    if self.text == self._text_placeholder:
                        self.text = ''

                    elif self.text == '':
                        self.text = self._text_placeholder

                def placeholder(self, text):
                    self._text_placeholder = text
                    self.text              = text

                    self.bound('on_focus', self._placeholder)

            return SInput

    @property
    def factoryLayout(self):
        '''
        Factory layout, this is factory for layouting application.
        '''
        if isinstance(self.baseclass, object) and self.baseclass is not None:
            class SLayout(self.baseclass):
                _part = []

                def gathering(self, part):
                    '''
                    this function is used to gathering widget or even layout for self layout
                    you can instance it as list or the object it self.
                    '''
                    if part is not None:
                        if isinstance(part, list):
                            self._part = []
                            for v in part:
                                self._part.append(v)

                        elif isinstance(part, object):
                                self._part.append(part)

                        return self

                @property
                def adding(self):
                    '''
                    this is a property for class to merge gathered items into it self.
                    '''
                    if self._part is not None:
                        for v in self._part:
                            self.add_widget(v)
                        return self

                @property
                def removing(self):
                    '''
                    same as above but this property is used to remove them.
                    '''
                    if self._part is not None:
                        for v in self._part:
                            self.remove_widget(v)
                        return self

            return SLayout

    @property
    def factoryModal(self):
        '''
        Factory layout, this is factory for popup, it class is inheritance from layout.
        '''
        if isinstance(self.baseclass, object) and self.baseclass is not None:
            class SModal(self.factoryLayout):
                _count_add = 0

                @property
                def adding(self):
                    '''
                    this is override property for popup adding.
                    '''
                    if self._part is not None:
                        for v in self._part:
                            if self._count_add < 1:
                                self._count_add += 1
                                self.add_widget(v)
                        return self

                @property
                def removingParts(self):
                    '''
                    same as above, but this override is do nothing.
                    '''
                    pass

            return SModal