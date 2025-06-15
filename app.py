from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from input import InputScr
from sitsscr import SitsScr
from resultscr import ResultScr
from test1scr import Test1Scr
from test2scr import Test2Scr


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScr())
        sm.add_widget(Test1Scr())
        sm.add_widget(SitsScr())
        sm.add_widget(Test2Scr())
        sm.add_widget(ResultScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm


app = MyApp()
app.run()