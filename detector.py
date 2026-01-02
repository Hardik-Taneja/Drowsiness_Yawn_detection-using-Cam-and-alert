import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist
from imutils import face_utils

EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 30
YAWN_THRESH = 20

COUNTER = 0

detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def lip_distance(shape):
    top = np.concatenate((shape[50:53], shape[61:64]))
    low = np.concatenate((shape[56:59], shape[65:68]))
    return abs(np.mean(top[:,1]) - np.mean(low[:,1]))

def analyze_frame(frame):
    global COUNTER

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector.detectMultiScale(gray, 1.1, 5)

    status = "SAFE"

    for (x, y, w, h) in rects:
        rect = dlib.rectangle(x, y, x+w, y+h)
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        ear = (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0
        yawn = lip_distance(shape)

        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                status = "DROWSY"
        else:
            COUNTER = 0

        if yawn > YAWN_THRESH:
            status = "YAWNING"

    return status
