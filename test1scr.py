from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from const import TEST_1
from timer import Timer


class Test1Scr(Screen):
    def __init__(self, name='test1'):
        super().__init__(name=name)
        self.counting = ObjectProperty()
        self.title = Label(text=TEST_1)
        self.timer = Timer(text='timer')
        self.timer.bind(done=self.timer_finished)
        pulse_input_txt = Label(text='pulse:')
        self.pulse_input_field = TextInput(hint_text='text')
        self.btn = Button(text="OK")
        self.btn.on_press = self.next

        pulse_input_line = BoxLayout(size_hint=(1, 0.7))
        pulse_input_line.add_widget(pulse_input_txt)
        pulse_input_line.add_widget(self.pulse_input_field)

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.title)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(pulse_input_line)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)

    def on_enter(self):
        self.title.text = TEST_1
        self.pulse_input_field.text = ''
        self.pulse_input_field.set_disabled(True)
        self.btn.set_disabled(True)
        self.timer.restart(15)

    def timer_finished(self, *args):
        self.pulse_input_field.set_disabled(False)
        self.btn.set_disabled(False)
        self.timer.event.cancel()

    def next(self):
        pulse = self.pulse_input_field.text
        if pulse == '' or int(pulse) <= 8 or int(pulse) >= 55:
            self.title.text = 'are you still alive how are you typing this press f'
        else:
            self.counting.p1 = int(pulse)
            self.manager.get_screen('sits').counting = self.counting
            self.manager.transition.direction = 'left'

            self.manager.current = 'sits'