import cv2
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_path = "yolov8n.pt", threshold_conf = 0.5):
        self.model = YOLO(model_path)
        self.model.to("cuda")
        self.threshold_conf = threshold_conf
        self.frame_count = 0
        self.last_detections = []
    
    def detect(self, frame):
        results = self.model(frame)
        self.frame_count +=1
        if self.frame_count % 5 != 0:
            return self.last_detections
        detections = []
        for box in results[0].boxes:
            conf = float(box.conf[0])
            if conf < self.threshold_conf:
                continue
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            label = self.model.names[cls_id]

            detections.append({
                "label" : label,
                "bbox" : (x1, y1, x2, y2),
                "confidence" : conf
            })
        self.last_detections = detections
        return detections