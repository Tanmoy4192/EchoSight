<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
</head>
<body>

<h1>EchoSight</h1>

<p>
EchoSight is a Python-based computer vision project that performs real-time scene analysis using a webcam.
It integrates object detection, OCR, depth estimation, and audio feedback in a modular pipeline.
</p>

<h2>Project Objective</h2>
<p>
The objective of this project is to understand how multiple computer vision components can be integrated
into a real-time system. The project is intended for learning and experimentation rather than production use.
</p>

<h2>Key Features</h2>
<ul>
    <li>Live video capture using OpenCV</li>
    <li>Real-time object detection using YOLO</li>
    <li>Approximate depth estimation based on visual heuristics</li>
    <li>Scene-level risk and navigation logic</li>
    <li>Text recognition using PaddleOCR</li>
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
│   └── ocr_reader.py      # OCR using PaddleOCR
│
├── vision/
│   ├── camera.py          # Webcam capture
│   ├── detector.py        # YOLO-based object detection
│   ├── depth.py           # Depth estimation logic
│   ├── scene.py           # Scene understanding
│   ├── fusion.py          # Feature fusion
│   ├── risk_fusion.py     # Risk assessment
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
    <li>PaddleOCR</li>
    <li>Text-to-Speech libraries</li>
</ul>

<h2>System Workflow</h2>
<ol>
    <li>Video frames are captured from the webcam.</li>
    <li>YOLO detects objects present in each frame.</li>
    <li>Depth estimation approximates object distance.</li>
    <li>Scene and risk analysis evaluate the environment.</li>
    <li>PaddleOCR extracts readable text when available.</li>
    <li>Relevant information is delivered through audio feedback.</li>
</ol>

<h2>How to Run</h2>
<ol>
    <li>Install the required Python dependencies.</li>
    <li>Ensure YOLO model files and PaddleOCR are properly configured.</li>
    <li>Connect a webcam.</li>
    <li>Run the application:
        <pre><code>python main.py</code></pre>
    </li>
</ol>

<h2>Limitations</h2>
<ul>
    <li>Depth estimation is approximate and not sensor-based.</li>
    <li>Detection accuracy depends on lighting and camera quality.</li>
    <li>OCR accuracy varies with text clarity and orientation.</li>
    <li>The system is not optimized for real-world assistive deployment.</li>
</ul>

<h2>Learning Outcomes</h2>
<ul>
    <li>Practical experience with YOLO and OpenCV</li>
    <li>Understanding real-time computer vision pipelines</li>
    <li>Integration of OCR and audio output</li>
    <li>Designing modular decision-making logic</li>
</ul>

<h2>Author</h2>
<p>
Tanmoy Samanta
</p>

<h2>Note</h2>
<p>
This project was developed for learning and demonstration purposes as part of hands-on practice
in computer vision and Python.
</p>

</body>
</html>