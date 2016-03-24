# Alias
***

Used to defining you layout, widget or controller into an informative and callable object. Most of alias information
is stored in `Alias.py` file. There's 2 types how to alias.

## Basic

    Alias.setInstance('layout', 'Welcome_Box', 'WelcomeBox@welcome')
    Alias.setInstance('widget', 'Welcome_Label', 'WelcomeLabel@welcome')
    Alias.setInstance('layout', 'Welcome_Control', 'WelcomeControl@welcome')
    
## One way

    Alias.setAll({
        'layout' : (['Welcome_Box', 'WelcomeBox@welcome'],
                    ['Welcome_Float', 'WelcomeFloat@welcome']),
        'widget' : (['Welcome_Label', 'WelcomeLabel@welcome'],
                    ['Welcome_Description', 'WelcomeDescription@welcome']),
        'controller' : (['Welcome_Control', 'WelcomeControl@welcome'],),
    })