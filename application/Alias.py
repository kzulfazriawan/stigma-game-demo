'''
ALIAS
=====
Alias module is used to define your application needed like layout, widget and
your controller.

:usage  : just put your needed stuff here, it'll sending into model or behavior
          class.

.. note::
    beware of misspelled key of your layout, widget or controller make sure you
    define them right.

see "Alias" documentation for more information.
'''
from core import Alias
# -- don't mind this comment, I just need to import my Layout, Widget and
# -- controller from my package alias ( it's a package not module class ).
# -- and then I need to set them into Alias
from application.alias import Layout, Widget, Controller

Alias.setAll({'layout': Layout,
              'widget': Widget,
              'controller': Controller
              })