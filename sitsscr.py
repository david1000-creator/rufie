from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

from algoritmica.mobile.rufie.timer import Timer
from const import SITS


class SitsScr(Screen):
    def __init__(self, name='sits'):
        super().__init__(name=name)
        self.counting = ObjectProperty()
        self.title = Label(text=SITS)
        self.timer = Timer(text='timer')
        self.timer.bind(done=self.timer_finished)
        self.btn = Button(text="OK")
        self.btn.on_press = self.next

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.title)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)

    def on_enter(self):
        self.title.text = SITS
        self.btn.set_disabled(True)
        self.timer.restart(45)

    def timer_finished(self, *args):
        self.btn.set_disabled(False)
        self.timer.event.cancel()

    def next(self):
        self.manager.get_screen('test2').counting = self.counting
        self.manager.transition.direction = 'left'

        self.manager.current = 'test2'