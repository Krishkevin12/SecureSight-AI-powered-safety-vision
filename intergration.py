import torch
import cv2
from deepface import DeepFace
import requests

# Load YOLOv5 model for weapon detection
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Flask server URL for sending alerts
ALERT_SERVER_URL = 'http://127.0.0.1:5000/send_alert'

# Open CCTV feed
cap = cv2.VideoCapture(0)  # Replace 0 with video path or CCTV feed URL

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Weapon detection
    results = model(frame)
    weapons_detected = False
    for pred in results.xyxy[0]:  # YOLO results for each detected object
        class_id = int(pred[5])  # Get class ID
        if class_id in [2, 3]:  # Weapon detection (e.g., guns, knives)
            weapons_detected = True
            print("Weapon detected!")
            # Send alert to Flask server
            requests.post(ALERT_SERVER_URL, json={"alert_type": "weapon"})

    # Panic detection
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = analysis['dominant_emotion']
        print(f"Detected Emotion: {dominant_emotion}")
        
        if dominant_emotion == 'fear':  # Panic detected
            print("Panic detected!")
            # Send alert to Flask server
            requests.post(ALERT_SERVER_URL, json={"alert_type": "panic"})
    except Exception as e:
        print(f"Error in emotion detection: {e}")

    # Show frame
    cv2.imshow('CCTV Feed', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
