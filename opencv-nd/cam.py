import kivy
import cv2 

from kivy.app import App 
from kivy.uix.camera import Camera
from kivy.graphics.texture import Texture


class CameraMain(Camera):
    firstFrame = None
    def _camera_loaded(self, *largs):
        if kivy.platform == 'android':
            self.texture = Texture.create(size=self.resolution,colorfmt='rgb')
            self.texture_size = list(self.texture.size)
        else:
            super(CameraMain, self)._camera_loaded()

    def on_tex(self, *l):
        if kivy.platform == 'android':
            buf = self._camera.grab_frame()
            if not buf:
                return
            frame = self._camera.decode_frame(buf)
            self.image = frame = self.process_frame(frame)
            buf = frame.tostring()
            self.texture.blit_buffer(buf, colorfmt = 'rgb', bufferfmt = 'ubyte')
        super(CameraMain, self).on_tex(*l)

    def process_frame(self, frame):
        r,g,b = cv2.split(frame)
        frame = cv2.merge((b,g,r))        
        rows,cols,channel = frame.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        dst = cv2.warpAffine(frame,M,(cols,rows))
        frame = cv2.flip(dst,1)
        if self.index == 1:
            frame = cv2.flip(dst,-1)

        return frame
