from kivy.app import App
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

        text = Label(text="123")
        self.add_widget(text)


class MyApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(MainScreen(name='main'))

        return sm
    
MyApp().run()


        
        
        

        

        