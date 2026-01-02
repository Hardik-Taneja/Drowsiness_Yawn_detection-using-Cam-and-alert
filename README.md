# 💤 Drowsiness & Yawn Detection System with Voice Alert

## 📌 Overview
This project is a real-time **driver monitoring system** that detects **drowsiness and yawning** using computer vision techniques and provides **instant voice alerts** to help prevent accidents caused by driver fatigue.

The system continuously analyzes a live webcam feed, monitors **eye closure duration** and **mouth opening**, and triggers an alert whenever signs of drowsiness or excessive yawning are detected.

This project is suitable for:
- 🚗 Driver safety systems
- 🚚 Fleet management applications
- 🛣️ Long-distance and night-time driving assistance

---

## 🎯 Features
- Real-time face detection using webcam
- Eye Aspect Ratio (EAR) based drowsiness detection
- Lip distance based yawn detection
- Voice alerts using text-to-speech
- Facial landmark visualization
- Lightweight and runs on CPU

---

## 🧠 How It Works

1. Captures live video stream from the webcam  
2. Detects face using Haar Cascade  
3. Extracts facial landmarks using Dlib  
4. Computes Eye Aspect Ratio (EAR)
   - Low EAR for consecutive frames → **Drowsiness Alert**
5. Measures lip distance
   - Large mouth opening → **Yawn Alert**
6. Generates real-time voice alerts

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:**
  - OpenCV
  - Dlib
  - NumPy
  - imutils
  - pyttsx3 (Text-to-Speech)
- **Model:** shape_predictor_68_face_landmarks.dat

---

## Dependencies

1. Python 3
2. opencv
3. dlib
4. imutils
5. scipy
6. numpy
7. argparse

## Run 

```
python drowsiness_yawn.py --webcam 0		//For external webcam, use the webcam number accordingly
```

## Setups

Change the threshold values according to your need
```
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 30
YAWN_THRESH = 10`	//change this according to the distance from the camera
```

## Authors

**Hardik Taneja** 


## Acknowledgments

* https://www.pyimagesearch.com/



