# Behavior
***

## What is behavior

the works is same as model but it has different function, behavior is used to organized "behavior" for application
into logic method. For example

    class Behavior(Behavior):
    
        def __init__(self):
            super(Behavior, self).__init__()
    
        def changeLabelText(self, parameter = None):
            '''
            Behavior function is used to change the label text on welcome.
            '''
            if self.widget.Welcome_Label.text == 'stigma':
                self.widget.Welcome_Label.text = 'Welcome, Build what you want fix what you need'
            else:
                self.widget.Welcome_Label.text = 'stigma'
    
        @property
        def alias(self):
            alias_map = CollectMap(
                change_label_text=eventAttach(self.changeLabelText, 'on_touch_down')
            )
    
            return alias_map.transform
            
as we see, we create an behavior called `changeLabelText` with parameter *None*, because the method is converted into
event *on_touch_down* with [eventAttach](#) helper, so when the widget called this method it will convert widget
`Welcome_Label` text

### alias property

this property is also had same function with [layer model property](#) but you can return the value with your own liking.