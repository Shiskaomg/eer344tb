from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class ScrButton(Button):
    def __init__(self, screen, diection="right", goal="main", **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self **kwargs):
        super().__init__
    

class MainScr(Screen):
    def __init__(self, **kwargs):
        vl = BoxLayout(orientation'vertical', padding-8, spacing-8)
        hl = BoxLayout()
        txt =  Label(text= 'Вибери екран')
        test_btn1 = Button(text = 'текстова кнопка')
        test_btn2 = Button(text = 'текстова кнопка')
        test_btn3 = Button(text = 'текстова кнопка')
        test_btn4 = Button(text = 'текстова кнопка')

        btn1 =


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))