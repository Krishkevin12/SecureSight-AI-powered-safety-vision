import torch
import cv2

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Pre-trained model

# Open CCTV feed (use video file or live feed)
cap = cv2.VideoCapture(0)  # Replace 0 with video path or CCTV feed URL

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Inference
    results = model(frame)

    # Display results
    results.show()

    # Filter for weapon detection (check for classes of interest)
    weapons_detected = False
    for pred in results.xyxy[0]:  # Results for each detected object
        class_id = int(pred[5])  # Get class ID (YOLO class index)
        if class_id in [2, 3]:  # Check for weapons (replace with actual weapon class IDs)
            weapons_detected = True
            print("Weapon detected!")
    
    # Show the frame with detection
    cv2.imshow('CCTV Feed', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
