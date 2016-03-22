from application import Application
from kivy.app import App


class MainApp(App):
    def __init__(self):
        '''
        Main Application or we call it Base Window Kivy.

        :return:
        '''
        super(MainApp, self).__init__()
        self._application = Application()

    def build(self):
        '''
        Everything we need to build constructed here.

        :return application class:
        '''

        return self._application

if __name__ == "__main__":
    MainApp().run()