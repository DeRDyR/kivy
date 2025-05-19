from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import random
import time




class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = 'Main'

        layout = BoxLayout(orientation='vertical')
        first_layout = BoxLayout()
        second_layout = BoxLayout(size_hint=(0.3, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        third_layout = BoxLayout(size_hint=(0.4, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.inp = TextInput(text="Переведите слово", font_size=25, size_hint=(0.3, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        word = Label(text="⠏⠗⠊⠺⠑⠞", font_size=50, font_name="DejaVuSans.ttf")
        self.check = Button(text='Проверить', font_size=30, size_hint=(0.3, 0.6), color=(0, 0, 1, 1), background_color=(0, 0, 1, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        first_layout.add_widget(word)
        second_layout.add_widget(self.inp)
        third_layout.add_widget(self.check)

        layout.add_widget(first_layout)
        layout.add_widget(second_layout)
        layout.add_widget(third_layout)

        self.add_widget(layout)

        self.check.on_press = self.press_button

    def press_button(self):

        text = self.inp.text

        if text.lower() == 'привет':
            self.go_screen_first()
        else:
            self.go_screen_second()


    def go_screen_first(self):
        self.manager.current = 'First'
    
    def go_screen_second(self):
        self.manager.current = "Second"

    

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        text = Label(text='Это правильный ответ!')

        self.add_widget(text)
    
class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        text = Label(text='Это неправильный ответ! Правильный ответ "Привет".')

        self.add_widget(text)

class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainScreen(name='Main'))
        sm.add_widget(FirstScreen(name='First'))
        sm.add_widget(SecondScreen(name='Second'))


        return sm
    
Window.size = (2560, 1440)
Window.top = 0
Window.left = 0
MyApp().run() 
        