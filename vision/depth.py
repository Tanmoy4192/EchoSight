from collections import deque

class DepthEstimator:
   
    def __init__(self, frame_height, frame_width,window_size = 5):
        # we use this because bbox size depends on resolution
        self.frame_height = frame_height
        self.frame_width = frame_width
        self.history = deque(maxlen = window_size)

    def estimate(self, bbox,label):
        scale = {
            "person": 0.15,
            "car" : 0.25,
            "chair" : 0.12
        }.get(label,0.18)

        frame_area = (self.frame_height*self.frame_width)
        x1, y1, x2, y2 = bbox
        h = y2 - y1
        w = x2 - x1
        area_ratio = (w*h) / frame_area

        self.history.append(area_ratio)
        avg_area_ratio = sum(self.history) / len(self.history)

        # thresholds proportional to frame 
        if avg_area_ratio > scale:
            return "very close"
        elif avg_area_ratio > scale * 0.6:
            return "close"
        else:
            return "far"
