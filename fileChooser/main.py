import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.button import Button
import os
from kivy.core.window import Window
Window.size = (1920, 1080)

# class MyWidget(BoxLayout):
#     def open(self, path, filename):
#         with open(os.path.join(path, filename[0])) as f:
#             print(f.read())

#     def selected(self, filename):
#         print("selected: %s" % filename[0])

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        button = Button(text="Open")
        button.pos_hint = {'center_x': .5}
        button.size_hint = (0.2, 0.2)
        files = FileChooserIconView(size=(1280, 640))
        # files.pos_hint = {'center_x':0.5,'center_y': 0.9}
        button.bind(on_press=self.check_files)
        layout.add_widget(button)
        layout.add_widget(files)
        return layout
    
    def check_files(self, *args):
        pass

if __name__ == '__main__':
    MyApp().run()