import kivy 
from kivy.app import App 
from kivy.lang import Builder 

class Main(App):
    def build(self):
        return Builder.load_file("cam.kv")
    

Main().run()