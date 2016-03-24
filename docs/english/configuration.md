# Configuration
***

## Preface
all the config value is stored in directory `config/` there's some python module you can use to set your application
such as `base.py` is used for set your basic application. so feel free to look through and edit it with you wanted.

## Base configuration
base configuration is pretty simple, you just need to reset the code into your liking because it's bounded with 
your application core. this is some example about dictionary variable inside file `base.py`:

main:{'path' : '/home/your path' , ...}

This is main configuration is used for your application so be careful with those value because it's not just bounded
but it's required for core application, there's some index key that you should set on your own, Here's some index key
in main variable

     - path, this key is used for managing your application `root path`, you can set it into default with value it with `None`, the application will automatically finding your root path.
     
graphics{'width': int width, height: int height, ...}
this variable is containing your graphics information like width, height and many more for your application.

      - width, this key will provide information window width, you can set it with you wanted to set but you only can set it as integer value for example `1024` if you wanted to change width your window application into 1024 pixel.

      - height, same as width but it used to manage your height window, you can only set it as integer value, for example `768` if you wanted to set your window application into 768 pixel.

kivy{'exit_on_escape': '0/1' , ...}
since stigma is build under kivy framework so you have to  follow the kivy rules. Here's some index key example on kivy

      - exit_on_escape, this key is provide for escape key function as the default of kivy configuration escape key will destroy the application, so you may set this key if you wanted to develop application for PC platform and the application will not destroy with just press escape button.
