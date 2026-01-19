from paddleocr import PaddleOCR
import cv2


class OCRReader:
    def __init__(self):
        # Speed-optimized OCR model
        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang='en'
        )

    def read(self, image):
        result = self.ocr.ocr(image)

        outputs = []
        if not result:
            return outputs

        for line in result[0]:
            text = None
            conf = None

            if isinstance(line[1], (list, tuple)) and len(line[1]) >= 2:
                text = line[1][0]
                conf = line[1][1]
            elif isinstance(line[1], str):
                text = line[1]
                conf = 1.0
            else:
                continue

            if conf < 0.6:
                continue

            outputs.append({
                "text": text,
                "confidence": round(conf, 2),
                "language": "en"
            })

        return outputs
