<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>EchoSight</h1>

<p>
EchoSight is a Python-based computer vision project that performs real-time scene analysis using a webcam.
It integrates object detection, text recognition, depth estimation, and audio feedback in a modular pipeline.
</p>

<h2>Project Objective</h2>
<p>
The objective of this project is to explore how multiple computer vision components can be combined
into a single real-time system. The focus is on system integration, event-driven logic,
and practical trade-offs rather than production-level accuracy.
</p>

<h2>Key Features</h2>
<ul>
    <li>Live video capture using OpenCV</li>
    <li>Real-time object detection using YOLO</li>
    <li>Approximate depth estimation based on visual heuristics</li>
    <li>Scene-level navigation and risk alerts</li>
    <li>On-demand text recognition using Tesseract OCR</li>
    <li>Audio feedback using text-to-speech</li>
</ul>

<h2>Project Structure</h2>
<pre>
EchoSight/
│
├── main.py                # Application entry point
├── audio/
│   └── speaker.py         # Text-to-speech handling
│
├── ocr/
│   └── ocr_reader.py      # OCR using Tesseract
│
├── vision/
│   ├── camera.py          # Webcam capture
│   ├── detector.py        # YOLO-based object detection
│   ├── depth.py           # Depth estimation logic
│   ├── scene.py           # Scene understanding
│   ├── fusion.py          # Feature fusion
│   ├── navigation.py      # Navigation decisions
│   └── decision.py        # Final decision logic
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

<h2>System Workflow</h2>
<ol>
    <li>Video frames are captured continuously from the webcam.</li>
    <li>YOLO detects objects present in the scene.</li>
    <li>Heuristic depth estimation approximates object distance.</li>
    <li>Navigation logic generates spoken alerts when risk conditions change.</li>
    <li>When the user presses the SPACE key, the current frame is captured.</li>
    <li>Tesseract OCR extracts printed text from the captured frame.</li>
    <li>The recognized text is spoken using text-to-speech.</li>
</ol>

<h2>How to Run</h2>
<ol>
    <li>Install Python dependencies listed in the project.</li>
    <li>Install Tesseract OCR and ensure it is added to the system PATH.</li>
    <li>Connect a webcam.</li>
    <li>Run the application:
        <pre><code>python main.py</code></pre>
    </li>
</ol>

<h2>Demo</h2>
<p>
A short demonstration video showing real-time object detection, live OCR on printed text
(triggered using the SPACE key), and audio feedback is available here:
</p>
<p>
<a href="PASTE_DEMO_VIDEO_LINK_HERE" target="_blank">Demo Video</a>
</p>

<h2>Limitations</h2>
<ul>
    <li>Depth estimation is heuristic and not sensor-based.</li>
    <li>OCR works best on printed text with good lighting and clarity.</li>
    <li>Handheld objects may be detected as persons by the object detector.</li>
    <li>The system is designed for demonstration and learning, not real-world assistive deployment.</li>
</ul>

<h2>Learning Outcomes</h2>
<ul>
    <li>Understanding real-time computer vision pipelines</li>
    <li>Integrating object detection, OCR, and audio feedback</li>
    <li>Designing event-driven logic in continuous video streams</li>
    <li>Managing trade-offs between accuracy, performance, and usability</li>
</ul>

<h2>Author</h2>
<p>
Tanmoy Samanta
</p>

<h2>Note</h2>
<p>
This project was developed for learning and demonstration purposes to explore applied
computer vision system design using Python.
</p>

</body>
</html>
