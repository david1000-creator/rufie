from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from const import*
from timer import Timer
class Test2Scr(Screen):
    def __init__(self, name='test2'):
        super().__init__(name=name)
        self.stage = 0
        self.counting = ObjectProperty()
        self.title = Label(text=TEST_3)

        self.timer1 = Timer(text='timer1')
        self.timer2 = Timer(text='timer2')
        self.timer3 = Timer(text='timer3')
        self.timer1.bind(done=self.timer_finished)
        self.timer2.bind(done=self.timer_finished)
        self.timer3.bind(done=self.timer_finished)

        pulse1_input_txt = Label(text='pulse1:')
        self.pulse1_input_field = TextInput(hint_text='text')

        pulse2_input_txt = Label(text='pulse2:')
        self.pulse2_input_field = TextInput(hint_text='text')
        self.btn = Button(text="OK", size_hint=(1, 0.5))
        self.btn.on_press = self.next

        timer_line = BoxLayout()
        timer_line.add_widget(self.timer1)
        timer_line.add_widget(self.timer2)
        timer_line.add_widget(self.timer3)

        pulse1_input_line = BoxLayout(size_hint=(1, 0.3))
        pulse1_input_line.add_widget(pulse1_input_txt)
        pulse1_input_line.add_widget(self.pulse1_input_field)

        pulse2_input_line = BoxLayout(size_hint=(1, 0.3))
        pulse2_input_line.add_widget(pulse2_input_txt)
        pulse2_input_line.add_widget(self.pulse2_input_field)

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.title)
        main_layout.add_widget(timer_line)
        main_layout.add_widget(pulse1_input_line)
        main_layout.add_widget(pulse2_input_line)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)

    def on_enter(self):
        self.stage = 0
        if self.timer1.done or self.timer2.done or self.timer3.done:
            self.timer1.done = False
            self.timer2.done = False
            self.timer3.done = False
        self.title.text = LOGIN_INSTRUCT
        self.pulse1_input_field.text = ''
        self.pulse2_input_field.text = ''
        self.pulse1_input_field.set_disabled(True)
        self.pulse2_input_field.set_disabled(True)
        self.btn.set_disabled(True)
        self.timer1.restart(15)


    def timer_finished(self, *args):
        if self.stage == 0:
            self.stage = 1
            self.pulse1_input_field.set_disabled(False)
            self.timer1.event.cancel()
            self.timer2.restart(30)
        elif self.stage == 1:
            self.stage = 2
            self.timer2.event.cancel()
            self.timer3.restart(15)
        else:
            self.pulse2_input_field.set_disabled(False)
            self.btn.set_disabled(False)
            self.timer3.event.cancel()


    def next(self):
        pulse = self.pulse1_input_field.text
        pulse2 = self.pulse2_input_field.text
        if pulse == '' or int(pulse) <= 8 or int(pulse) >= 55 or pulse2 == '' or int(pulse2) <= 8 or int(pulse2) >= 55:
            self.title.text = ('are you still alive how are you typing this press f')

        else:
            self.counting.p2 = int(pulse)
            self.counting.p3 = int(pulse2)
            self.counting.total_score()
            self.manager.get_screen('result').counting = self.counting
            self.manager.transition.direction = 'left'

            self.manager.current = 'result'