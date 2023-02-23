from kivy.app import App 
from kivy.uix.camera import Camera 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 

class SelfieCameraApp(App):

    def build(self):

        '''
        :return:
        '''

        # Camera.
        self.camera_obj = Camera()
        self.camera_obj.play = True
        self.camera_obj.resolution = (640,480)

        # Button.
        button_obj = Button(text="Click Here")
        button_obj.size_hint = (.5, .2)
        button_obj.pos_hint = {'x':.25, 'y':.25}
        button_obj.bind(on_press=self.take_selfie)

        # Layout.
        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)

        return layout
    

    def take_selfie(self, *args):
        self.camera_obj.export_to_png("./image.png")


if __name__ == "__main__":
    SelfieCameraApp().run()