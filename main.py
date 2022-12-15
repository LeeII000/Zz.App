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
import math

class FirstScreen(Screen):
    def play_music(self):
        music = SoundLoader.load('songs/an_ending.mp3')

        if music:
            music.loop = True
            music.play()  

class EndingScreen(Screen):
    pass

class OptionScreen(Screen):
    def play1(self):
        music = SoundLoader.load('songs/an_ending.mp3')

        if self.ids.music1.state == 'down':
            self.ids.music1.text = "1"
            music.play()
        else:
            music.unload()

    def play2(self):
        music = SoundLoader.load('songs/rain.mp3')

        if music:
            music.loop = True
            music.play()
    
    def play3(self):
        music = SoundLoader.load('songs/3.mp3')

        if music:
            music.loop = True
            music.play()

    def play4(self):
        music = SoundLoader.load('songs/fire.mp3')

        if music:
            music.loop = True
            music.play()

class OptionWidget(BoxLayout):
    pass

class Ingame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  

    def stop_music(self):
        music = SoundLoader.load('songs/an_ending.mp3')

        music.play()
        music.stop()
        music.unload()

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

class Music(Sound):
    def music1(self):
        music1 = SoundLoader.load('songs/an_ending.mp3')

    def music2(self):
        music2 = SoundLoader.load('songs/rain.mp3')

    def music3(self):
        music3 = SoundLoader.load('songs/3.mp3')

    def music4(self):
        music4 = SoundLoader.load('songs/fire.mp3')

class SCManager(ScreenManager):
    pass
            
class MainApp(App):
    pass

MainApp().run()
