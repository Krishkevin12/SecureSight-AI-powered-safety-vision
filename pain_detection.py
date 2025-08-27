from deepface import DeepFace
import cv2

# Open CCTV feed
cap = cv2.VideoCapture(0)  # Replace 0 with video path or CCTV feed URL

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform emotion detection
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        dominant_emotion = analysis['dominant_emotion']
        print(f"Detected Emotion: {dominant_emotion}")
        
        # If panic (fear) is detected, take action
        if dominant_emotion == 'fear':
            print("Panic detected!")
            # Trigger an alert (e.g., send to Flask server)
    except Exception as e:
        print(f"Error in emotion detection: {e}")

    # Show the frame with emotion detection
    cv2.imshow('CCTV Feed - Emotion Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
