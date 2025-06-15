from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from const import LOGIN_INSTRUCT
from counting import Counting


class InputScr(Screen):
    def __init__(self, name='input'):
        super().__init__(name=name)

        self.title = Label(text=LOGIN_INSTRUCT)
        name_input_txt = Label(text='name:')
        self.name_input_field = TextInput(hint_text='text')

        age_input_txt = Label(text='age:')
        self.age_input_field = TextInput(hint_text='text')
        btn = Button(text="OK", size_hint=(1, 0.3))
        btn.on_press = self.next

        name_input_line = BoxLayout(size_hint=(1, 0.3))
        name_input_line.add_widget(name_input_txt)
        name_input_line.add_widget(self.name_input_field)

        age_input_line = BoxLayout(size_hint=(1, 0.3))
        age_input_line.add_widget(age_input_txt)
        age_input_line.add_widget(self.age_input_field)

        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.title)
        main_layout.add_widget(name_input_line)
        main_layout.add_widget(age_input_line)
        main_layout.add_widget(btn)

        self.add_widget(main_layout)
    def on_enter(self):
        self.title.text = LOGIN_INSTRUCT
        self.name_input_field.text = ''
        self.age_input_field.text = ''
    def next(self):
        if not self.name_input_field.text.strip():
            self.title.text = ('enter name!')
        else:
            age = self.age_input_field.text
            if age == '' or int(age) <= 7 or int(age) >= 120:
                self.title.text = ('can\'t check this age')
            else:
                counting = Counting(self.name_input_field.text, int(age))
                self.manager.get_screen('test1').counting = counting
                self.manager.transition.direction = 'right'
                self.manager.current = 'test1'