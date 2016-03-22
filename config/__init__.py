from os import path
import base

# -- APPLICATION CONFIGURATION
configuration_app = {
    'graphics': base.graphics,
    'kivy': base.kivy
}

if base.main['path'] is None:
    # -- Current file directory is config/, I need to up into self directory.
    configuration_root = path.dirname(path.dirname(path.realpath(__file__)))
else:
    configuration_root = base.main['path']

# -- ALIAS PATH CONFIGURATION
configuration_path = {
    'config': path.dirname(path.realpath(__file__))
}

# -- CONDITIONAL OF PATH CONFIGURATION.
if base.main['path'] is None:
    configuration_path['root'] = path.dirname(configuration_path['config'])
else:
    configuration_path['root'] = base.main['path']

configuration_path['core'] = path.join(configuration_path['root'], 'core')
configuration_path['library'] = path.join(configuration_path['root'], 'library')
configuration_path['application'] = path.join(configuration_path['root'], 'application')

