from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import BooleanProperty


class Timer(Label):
    done = BooleanProperty(False)

    def __init__(self, total=15, **kwargs):
        super().__init__(**kwargs)
        self.current = total
        self.text = f'{self.current} sec'
        self.event = None

    def start(self):
        self.event = Clock.schedule_interval(self.change, 1)

    def change(self, dt):
        self.current -= 1
        self.text = f'{self.current} sec'
        if self.current == 0:
            self.done = True
            return False

    def restart(self, total):
        if self.event:
            self.event.cancel()
        self.current = total
        self.text = f'{self.current} sec'
        self.done = False
        self.start()