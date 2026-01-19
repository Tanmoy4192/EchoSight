import cv2
#take input from camera and gives out put the resized frames
class Camera:
    def __init__(self, index=0, width=640, height=480):
        self.cap = cv2.VideoCapture(index) #capturing the video from web cam, using 1 to use secondary cam
        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera.") 
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width) #resized width
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #resized height

    def get_frame(self):
        ret, frame = self.cap.read() 
        if not ret:
            raise RuntimeError("Failed to read frame from camera.")
        return frame

    def release(self):
        self.cap.release()