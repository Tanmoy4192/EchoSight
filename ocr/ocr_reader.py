import cv2
import pytesseract

class OCRReader:
    def __init__(self):
        pass

    def read(self, image):
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Increase contrast
        gray = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

        # Slight blur to remove noise
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        # Tesseract config:
        # --psm 6 = assume a block of text
        config = "--oem 3 --psm 6"

        text = pytesseract.image_to_string(gray, config=config)

        # Clean output
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        return lines
