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

class OptionScreen(Screen):
    pass

class IngameBlue(Screen, Widget):
     def __init__(self, **kwargs):
        super().__init__(**kwargs)

     def Volume_Blue(self, widget): 
        if widget.state == "normal":
            if self.parent.ids.mus1.song.state == "play":
                self.parent.ids.mus1.volume_one()
                print("i")
            elif self.parent.ids.mus2.song.state == "play":
                self.parent.ids.mus2.volume_one()
            elif self.parent.ids.mus3.song.state == "play":
                self.parent.ids.mus3.volume_one()
            else:
                self.parent.ids.mus4.volume_one()
        else:
            if self.parent.ids.mus1.song.state == "play":
                self.parent.ids.mus1.volume_Zero()
                print("i")
            elif self.parent.ids.mus2.song.state == "play":
                self.parent.ids.mus2.volume_Zero()
            elif self.parent.ids.mus3.song.state == "play":
                self.parent.ids.mus3.volume_Zero()
            else:
                self.parent.ids.mus4.volume_Zero()


class IngamePink(Screen, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Volume_Pink(self, widget): 
        if widget.state == "normal":
            if self.parent.ids.mus1.song.state == "play":
                self.parent.ids.mus1.volume_one()
            elif self.parent.ids.mus2.song.state == "play":
                self.parent.ids.mus2.volume_one()
            elif self.parent.ids.mus3.song.state == "play":
                self.parent.ids.mus3.volume_one()
            else:
                self.parent.ids.mus4.volume_one()
        else:
            if self.parent.ids.mus1.song.state == "play":
                self.parent.ids.mus1.volume_Zero()
            elif self.parent.ids.mus2.song.state == "play":
                self.parent.ids.mus2.volume_Zero()
            elif self.parent.ids.mus3.song.state == "play":
                self.parent.ids.mus3.volume_Zero()
            else:
                self.parent.ids.mus4.volume_Zero()

 

class IngameGreen(Screen, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Volume_Green(self, widget): 
        if widget.state == "normal":
            if self.parent.ids.mus1.song.state == "play":
                self.parent.ids.mus1.volume_one()
            elif self.parent.ids.mus2.song.state == "play":
                self.parent.ids.mus2.volume_one()
            elif self.parent.ids.mus3.song.state == "play":
                self.parent.ids.mus3.volume_one()
            else:
                self.parent.ids.mus4.volume_one()
        else:
            if self.parent.ids.mus1.song.state == "play":
                self.parent.ids.mus1.volume_Zero()
            elif self.parent.ids.mus2.song.state == "play":
                self.parent.ids.mus2.volume_Zero()
            elif self.parent.ids.mus3.song.state == "play":
                self.parent.ids.mus3.volume_Zero()
            else:
                self.parent.ids.mus4.volume_Zero()



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
            self.sheep.pos = (x+2,math.sin(x)*2+50)

    def on_touch_up(self, touch):
        super().on_touch_up(touch)
        a_delay = 0.05
        if touch.osx > 0 and touch.osy < 0.9:
            x = -100
            y = 50
            self.sheep.pos = (x,y)

class Music1(Widget):
    song = SoundLoader.load('songs/rain.mp3')
    def music1(self):

        if Music1.song.state == 'stop':
            Music1.song.play()
        else:
            Music1.song.stop()
            Music1.song.unload()
            
    def volume_Zero(self):
        Music1.song.volume = 0
    def volume_one(self):
        Music1.song.volume = 1

class Music2(Widget):
    song = SoundLoader.load('songs/fire.mp3')
    def music2(self):

        if Music2.song.state == 'stop':
            Music2.song.play()
        else:
            Music2.song.stop()
            Music2.song.unload()
            
    def volume_Zero(self):
        Music2.song.volume = 0
    def volume_one(self):
        Music2.song.volume = 1

class Music3(Widget):
    song = SoundLoader.load('songs/3.mp3')
    def music3(self):

        if Music3.song.state == 'stop':
            Music3.song.play()
        else:
            Music3.song.stop()
            Music3.song.unload()

    def volume_Zero(self):
        Music3.song.volume = 0
    def volume_one(self):
        Music3.song.volume = 1

class Music4(Widget):
    song = SoundLoader.load('songs/an_ending.mp3')
    def music4(self):

        if Music4.song.state == 'stop':
            Music4.song.play()
        else:
            Music4.song.stop()
            Music4.song.unload()

    def volume_Zero(self):
        Music4.song.volume = 0
    def volume_one(self):
        Music4.song.volume = 1

class SCManager(ScreenManager):
    pass
            
class MainApp(App):
    pass

MainApp().run()

