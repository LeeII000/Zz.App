from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import Clock
from kivy.metrics import dp
from kivy.graphics import Rectangle
import math

class FirstScreen(Screen):
    pass

class EndingScreen(Screen):
    pass

class OptionScreen(Screen):
    pass

class OptionWidget(BoxLayout):
    pass

class Ingame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)           

class Sheep(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sheep_size = dp(100)
        with self.canvas:
            self.sheep = Rectangle(pos=self.center,size=(self.sheep_size,self.sheep_size),source = "images/prototype-10.png")
        Clock.schedule_interval(self.pose,1/10)
        global x,y
        
    def pose(self,dt):
        x,y = self.sheep.pos 
        if x >= 130:
            self.sheep.pos = (x,y)
        else:
            self.sheep.pos = (x+2,math.sin(x)*2+100)
        
    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        a_delay = 0.05
        if touch.osx > 0 and touch.osy < 0.9:
            x = -100
            y = 50
            self.sheep.pos = (x,y)
   

class SCManager(ScreenManager):
    pass
            
class MainApp(App):

    pass

MainApp().run()
