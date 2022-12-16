from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.video import Video
from kivy.core.audio import SoundLoader, Sound
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import Clock
from kivy.metrics import dp
from kivy.graphics import Rectangle
from kivy.uix.togglebutton import ToggleButton
import math

class FirstScreen(Screen):
    pass

class EndingScreen(Screen):
    pass

class OptionScreen(Screen):
    pass

class IngameBlue(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class IngamePink(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class IngameGreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  

class Sheep(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sheep_size = dp(120)
        with self.canvas:
            self.sheep = Rectangle(pos=self.center,size=(self.sheep_size,self.sheep_size),source = "images/prototype-10.png")
        Clock.schedule_interval(self.pose,1/10)
        global x,y
        
    def pose(self,dt):
        x,y = self.sheep.pos 
        if x >= 250:
            self.sheep.pos = (x,y)
        else:
            self.sheep.pos = (x+2,math.sin(x)*2+240)
        
    def on_touch_down(self, touch):
        super().on_touch_down(touch)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        a_delay = 0.05
        if touch.osx > 0 and touch.osy < 0.9:
            x = -100
            y = 50
            self.sheep.pos = (x,y)

class Music1(Widget):
    song1 = SoundLoader.load('songs/rain.mp3')
    def music1(self):

        if Music1.song1.state == 'stop':
            Music1.song1.play()
        else:
            Music1.song1.stop()
            Music1.song1.unload()

class Music2(Widget):
    song2 = SoundLoader.load('songs/fire.mp3')
    def music2(self):

        if Music2.song2.state == 'stop':
            Music2.song2.play()
        else:
            Music2.song2.stop()
            Music2.song2.unload()

class Music3(Widget):
    song3 = SoundLoader.load('songs/3.mp3')
    def music3(self):

        if Music3.song3.state == 'stop':
            Music3.song3.play()
        else:
            Music3.song3.stop()
            Music3.song3.unload()

class Music4(Widget):
    song4 = SoundLoader.load('songs/an_ending.mp3')
    def music4(self):

        if Music4.song4.state == 'stop':
            Music4.song4.play()
        else:
            Music4.song4.stop()
            Music4.song4.unload()

class SCManager(ScreenManager):
    pass
            
class MainApp(App):
    pass

MainApp().run()
