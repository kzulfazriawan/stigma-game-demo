# Model
***

##  What is model

Instead you defining your layout and widget into `Alias` you may need to organized them into a beautiful pieces.
Model is used to grouping your layout and widget into a logic method. Here's the sample code

    class Model(Model):
        def __init__(self):
            super(Model, self).__init__()
        
        def welcome(self):
        '''
        Model function to showing welcome message when application running.
        '''
        self.layout.Welcome_Box.gathering([self.widget.Welcome_Label])
        self.layout.Welcome_Box.adding

        return self.layout.Welcome_Box
        
        @property
        def layer(self):
            return [self.welcome()]        
        
we organized `layout Welcome_Box` and `widget Welcome_Label` into an display model called ***welcome***.
all the function model is stored into `Model` class and after the function is created it need to defined into
`layer` property as list.

### layer property
this is required method for model class, since it got inheritance from abstract Model class from core and also
the return only honor list. here's some example to explain how's layer works.