from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class ResultScr(Screen):
    def __init__(self, name='result'):
        super().__init__(name=name)
        self.counting = ObjectProperty()
        self.title = Label(text='title')
        btn = Button(text="OK")
        btn.on_press = self.next

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.title)
        main_layout.add_widget(btn)

        self.add_widget(main_layout)

    def on_enter(self):
        self.title.text = str(self.counting)

    def next(self):
        self.manager.transition.direction = 'left'

        self.manager.current = 'input'