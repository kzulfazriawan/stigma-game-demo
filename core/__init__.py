'''
initialize the core bundle
==========================

:module : this module will initialize class core.

in this parts all core class would be initialized with their parameter,
so when you call it you dont have to attach it with variable parameter.
'''
import os

from config import configuration_root, configuration_app
from files import Files
from application import Alias
from window import Windows
from behavior import Behavior
from model import Model

Files = Files(root = configuration_root,
              core = os.path.join(configuration_root, 'core'),
              apps = os.path.join(configuration_root, 'application'),
              conf = os.path.join(configuration_root, 'config'),
              libs = os.path.join(configuration_root, 'library'))

Windows = Windows(app= configuration_app).setWindow

Alias = Alias('application' , Files.getClass)