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

    camera = Camera(index=2, width=1280, height=720)
    detector = ObjectDetector(model_path="yolov8n.pt", threshold_conf=0.5)

    speaker = Speaker()
    scene = SceneDescriber()
    decision = decisionEngine()
    navigation = NavigationEngine()

    depth = DepthEstimator(frame_height=240, frame_width=320)
    ocr_reader = OCRReader()

    fusion = None
    last_action = None
    last_nav_sentence = None
    nav_pause_until = 0
    NAV_PAUSE_SECONDS = 4
    prev_time = time.time()

    while True:

        raw_frame = camera.get_frame()
        if raw_frame is None:
            break

        frame = cv2.resize(raw_frame, (320, 240))

        if fusion is None:
            _, width, _ = frame.shape
            fusion = Fusion(width)

        # -------- OBJECT DETECTION --------
        detections = detector.detect(frame)
        detections_with_meta = []

        for detection in detections:
            bbox = detection["bbox"]

            detection["position"] = fusion.get_position(bbox)
            detection["distance"] = depth.estimate(bbox, detection["label"])
            detections_with_meta.append(detection)

            x1, y1, x2, y2 = bbox
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        selected = decision.selection(detections_with_meta)
        nav_action = navigation.decide(detections_with_meta)

        cv2.imshow("EchoSight - camera feed", frame)
        key = cv2.waitKey(1) & 0xFF

        # -------- OCR ON SPACE (LIVE FRAME) --------
        if key == 32:  # SPACE
            ocr_frame = raw_frame.copy()

            ocr_results = ocr_reader.read(ocr_frame)

            if not ocr_results:
                sentence = "No text detected"
            else:
                sentence = " ".join(ocr_results)
                print("OCR:", sentence)

            speaker.say(sentence)
            nav_pause_until = time.time() + NAV_PAUSE_SECONDS


            # IMPORTANT: prevent navigation speech this frame
            continue

        elif key == ord("q"):
            break

        # -------- NAVIGATION SPEECH --------
        sentence = None

        if selected:
            sentence = scene.describe_object(selected)
        elif nav_action and nav_action != last_action:
            sentence = scene.describe_navigation(nav_action)
            last_action = nav_action

            # Speak ONLY if sentence changed
        if (sentence and sentence != last_nav_sentence and time.time() > nav_pause_until):
            speaker.say(sentence)
            last_nav_sentence = sentence

        # -------- FPS --------
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

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
