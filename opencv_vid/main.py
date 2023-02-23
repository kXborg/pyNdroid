from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout 
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import kivy 


class MainApp(MDApp):


    def build(self):
        layout = MDBoxLayout(orientation="vertical")
        self.image = Image()
        self.save_img_button = MDRaisedButton(
            text = "Click",
            pos_hint = {'center_x': .5, 'center_y': .5},
            size_hint = (None, None)
        )
        self.save_img_button.bind(on_press=self.take_picture)

        layout.add_widget(self.image)
        layout.add_widget(self.save_img_button)

        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1/30.0)

        return layout
    

    def load_video(self, *args):
        ret, frame = self.capture.read()
        # Frame Init.
        self.image_frame = frame
        # put some text.
        cv2.putText(frame, 'Text', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)

        # Convert to buffer.
        buffer = cv2.flip(frame, 0).tostring()
        # Create texture.
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        # Blit buffer.
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        # put texture in image texture data.
        self.image.texture = texture
    

    def take_picture(self, *args):
        image_name = "image-2.jpg"
        cv2.imwrite(image_name, self.image_frame)


if __name__ == "__main__":
    MainApp().run()