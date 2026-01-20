
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>EchoSight</h1>

<p>
EchoSight is a Python-based computer vision project that performs real-time scene analysis using a webcam.
The system combines object detection, heuristic depth estimation, text recognition, and audio feedback
to simulate how an assistive vision pipeline can be designed and coordinated.
</p>

<h2>Project Objective</h2>
<p>
The objective of this project is to understand how multiple computer vision modules can be integrated
into a single real-time application. The focus is on system-level design, decision logic,
and managing competing outputs such as navigation alerts and OCR feedback.
The project is intended for learning and demonstration purposes.
</p>

<h2>Key Features</h2>
<ul>
    <li>Live video capture using OpenCV</li>
    <li>Real-time object detection using YOLO</li>
    <li>Approximate depth estimation using bounding-box heuristics</li>
    <li>Rule-based navigation and risk alerts</li>
    <li>On-demand text recognition using Tesseract OCR</li>
    <li>Spoken feedback using text-to-speech</li>
</ul>

<h2>Project Structure</h2>
<pre>
EchoSight/
│
├── main.py                # Application entry point and control logic
├── audio/
│   └── speaker.py         # Text-to-speech output
│
├── ocr/
│   └── ocr_reader.py      # Printed text recognition using Tesseract
│
├── vision/
│   ├── camera.py          # Webcam capture
│   ├── detector.py        # YOLO-based object detection
│   ├── depth.py           # Heuristic depth estimation
│   ├── fusion.py          # Spatial fusion (left / center / right)
│   ├── scene.py           # Scene description logic
│   ├── navigation.py      # Navigation decision rules
│   └── decision.py        # Priority-based object selection
│
└── __init__.py
</pre>

<h2>Technologies Used</h2>
<ul>
    <li>Python 3</li>
    <li>OpenCV</li>
    <li>YOLO (object detection)</li>
    <li>Tesseract OCR (printed text recognition)</li>
    <li>pyttsx3 (text-to-speech)</li>
</ul>

<h2>System Logic and Design</h2>

<h3>Object Detection and Spatial Positioning</h3>
<p>
Each video frame is processed by YOLO to detect objects such as people and obstacles.
Detected bounding boxes are spatially classified as left, center, or right based on
their horizontal position in the frame. This spatial information is later used
to generate navigation instructions.
</p>

<h3>Depth Estimation</h3>
<p>
Depth is estimated using a heuristic approach based on bounding box size.
Larger bounding boxes are interpreted as closer objects, while smaller boxes
are treated as farther away. This approximation does not rely on sensors
and is intended to provide relative distance cues rather than exact measurements.
</p>

<h3>Decision and Navigation Logic</h3>
<p>
Detected objects are filtered and prioritised using rule-based logic.
Objects closer to the center of the frame and at shorter estimated distances
are treated as higher risk. Navigation alerts are generated only when the
detected scene changes, which prevents repeated speech for the same condition.
</p>

<h3>Speech Priority Handling</h3>
<p>
The system distinguishes between continuous navigation states and event-driven actions.
Navigation alerts are spoken only when the risk state changes.
When OCR is triggered, navigation speech is temporarily suppressed to ensure
clear and uninterrupted audio output.
</p>

<h3>OCR Workflow</h3>
<p>
Text recognition is performed on demand rather than continuously.
When the user presses the SPACE key, the current video frame is captured
and passed to Tesseract OCR. This design avoids unstable OCR output
from live video and improves readability for printed text.
The recognized text is then spoken using text-to-speech.
</p>

<h2>System Workflow</h2>
<ol>
    <li>Video frames are captured continuously from the webcam.</li>
    <li>YOLO detects objects present in the scene.</li>
    <li>Bounding-box heuristics estimate relative object distance.</li>
    <li>Navigation rules evaluate risk and generate spoken alerts when needed.</li>
    <li>The user presses SPACE to trigger OCR.</li>
    <li>The current frame is captured and processed by Tesseract.</li>
    <li>Recognized text is spoken, and navigation resumes afterward.</li>
</ol>

<h2>How to Run</h2>
<ol>
    <li>Install the required Python dependencies.</li>
    <li>Install Tesseract OCR and add it to the system PATH.</li>
    <li>Connect a webcam.</li>
    <li>Run the application:
        <pre><code>python main.py</code></pre>
    </li>
</ol>

<h2>Demo</h2>
<p>
A short demonstration video showing real-time object detection, rule-based navigation alerts,
and live OCR on printed text (triggered using the SPACE key) is available here:
</p>
<p>
<a href="https://drive.google.com/file/d/13KHyXgGuLDqJiVFZ60mSzFhYdSkc4pbX/view?usp=sharing" target="_blank">Demo Video</a>
</p>

<h2>Limitations</h2>
<ul>
    <li>Depth estimation is heuristic and not sensor-based.</li>
    <li>Navigation rules are manually defined and not learned.</li>
    <li>OCR works best on clear printed text with stable lighting.</li>
    <li>Hands or books may be detected as persons due to model limitations.</li>
    <li>The system is designed for learning and demonstration, not deployment.</li>
</ul>

<h2>Learning Outcomes</h2>
<ul>
    <li>Designing real-time computer vision pipelines</li>
    <li>Combining detection, depth heuristics, and rule-based logic</li>
    <li>Handling competing audio outputs in continuous systems</li>
    <li>Understanding practical OCR constraints in video streams</li>
</ul>

<h2>Author</h2>
<p>
Tanmoy Samanta
</p>

<h2>Note</h2>
<p>
This project was developed as a hands-on learning exercise to explore
applied computer vision system design using Python.
</p>

</body>
</html>
