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

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        





class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        first_layout = BoxLayout()
        second_layout = BoxLayout()

        text = TextInput(text="Переведите слово", font_size=25, size_hint=(0.6, 0.4))
        word = Label(text="⠏⠗⠊⠺⠑⠞", font_size=50)
        check = Button(text='Проверить')

        first_layout.add_widget(word)
        second_layout.add_widget(text)
        second_layout.add_widget(check)

        layout.add_widget(first_layout)
        layout.add_widget(second_layout)

        self.add_widget(layout)

        text = text.text

        


        


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainScreen(name='main'))

        return sm
    
Window.size = (2560, 1440)
Window.top = 0
Window.left = 0
MyApp().run()


        
        
        

        

        