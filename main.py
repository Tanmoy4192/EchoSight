import cv2
import time

from vision.camera import Camera
from vision.detector import ObjectDetector
from vision.depth import DepthEstimator         
from vision.fusion import Fusion
from vision.scene import SceneDescriber
from vision.decision import decisionEngine
from vision.navigation import NavigationEngine

from audio.speaker import Speaker
from ocr.ocr_reader import OCRReader


def main():

    # ----- core components -----
    camera = Camera()
    detector = ObjectDetector(model_path="yolov8n.pt", threshold_conf=0.5)

    # audio + logic
    speaker = Speaker(cooldown=2)
    scene = SceneDescriber()
    decision = decisionEngine()
    navigation = NavigationEngine()

    # lightweight bbox-based distance estimator
    depth = DepthEstimator(frame_height=240,frame_width = 320)    

    # OCR
    ocr_reader = OCRReader()

    fusion = None
    last_action = None
    prev_time = time.time()
    activate_ocr = False

    while True:

        frame = camera.get_frame()
        if frame is None:
            break

        # lower resolution = higher FPS
        frame = cv2.resize(frame, (320, 240))

        # initialise fusion once
        if fusion is None:
            _, width, _ = frame.shape
            fusion = Fusion(width)

        # -------- OBJECT DETECTION --------
        detections = detector.detect(frame)
        detections_with_meta = []

        for detection in detections:
            bbox = detection["bbox"]

            # LEFT / RIGHT / AHEAD
            detection["position"] = fusion.get_position(bbox)

            # distance using bbox height estimator
            detection["distance"] = depth.estimate(bbox,detection["label"])

            detections_with_meta.append(detection)

            # draw bbox on screen
            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f'{detection["label"]} {detection["confidence"]:.2f} {detection["distance"]}',
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )

        # decision making
        selected = decision.selection(detections_with_meta)
        nav_action = navigation.decide(detections_with_meta)

        sentence = None
        #adding ocr
        key = cv2.waitKey(1) & 0xFF     

        if key ==32: #space button to activate
            activate_ocr = True

        elif key == ord("q"):
            break

        if activate_ocr == True:
            ocr_results = ocr_reader.read(frame)
            speaker.say("Reading text")
            for result in ocr_results:
                print(result["text"])
                speaker.say(result["text"])
            activate_ocr = False #reset after using

        # -------- PRIORITY LOGIC --------
        if not sentence and selected:
            sentence = scene.describe_object(selected)

        elif not sentence and nav_action and nav_action != last_action:
            sentence = scene.describe_navigation(nav_action)
            last_action = nav_action
 
        if nav_action is None:
            last_action = None

        if sentence:
            speaker.say(sentence)

        # -------- FPS display --------
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        cv2.putText(
            frame,
            f"FPS: {int(fps)}",
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            2,
        )

        cv2.imshow("EchoSight - camera feed", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
