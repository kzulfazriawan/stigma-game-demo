'''
Application
===========
in this module, you will see many class but nothing inside of, all that
class is product from factory application for your widget, layout, etc
inheritance.

:usage  : if you really need to use it, just import this module, and put
          any class you wanted into your widget or layout.

.. note::
    you only can put them only once in a class, say you wanted to make
    2 different button but with only 1 imported class, please don't do
    that ! you can't put a class already had a subclass into another
    subclass.
'''
from kivy.uix import label, button, image, listview, \
    textinput, togglebutton, \
    boxlayout, floatlayout, anchorlayout, gridlayout, modalview, popup
from factory import ApplicationFactory


# -- Start of create widget class.
class Button(ApplicationFactory(button.Button).factoryWidget):
    '''
    If you want to create a button, or something can be pressed, or touched
    you better use button.
    '''
    pass


class Image(ApplicationFactory(image.Image).factoryWidget):
    '''
    Adding some image to beautify you application is a nice idea.
    '''
    pass


class Label(ApplicationFactory(label.Label).factoryWidget):
    '''
    If there's any text you want to display then use this Label class.
    '''
    pass


class Radio(ApplicationFactory(togglebutton.ToggleButton).factoryWidget):
    '''
    Radio, you know what it used for.
    '''
    pass


# -- End of create widget class.
# -- Start of create layout class.
class Anchor(ApplicationFactory(anchorlayout.AnchorLayout).factoryLayout):
    '''
    An anchor fixed layout for your application room
    '''
    pass


class Box(ApplicationFactory(boxlayout.BoxLayout).factoryLayout):
    '''
    Box is regular layout for application room.
    '''
    pass


class Float(ApplicationFactory(floatlayout.FloatLayout).factoryLayout):
    '''
    it's a magic float room, you can use to manage you widget freely without limit.
    '''
    pass


class Grid(ApplicationFactory(gridlayout.GridLayout).factoryLayout):
    '''
    If you prefer to use grid display, use Grid for layout.
    '''
    pass

class Modal(ApplicationFactory(modalview.ModalView).factoryModal):
    '''
    Modal is layout you can use for showing and hide it in temporray ways, modal is
    different than the other layout when you create it in function model you no need
    to adding the into collection
    '''
    pass

class Popup(ApplicationFactory(popup.Popup).factoryModal):
    '''
    Popup is also modal but it the layout is not like the other layout, it can add only
    one widget or layout inside it.
    '''
    pass

# -- End of create layout class.
# -- Start of create Input class.
class Input(ApplicationFactory(textinput.TextInput).factoryInput):
    '''
    Say if you want to create a input like login input for your application
    you will gonna use this.
    '''
    pass