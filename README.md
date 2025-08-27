

# 🛡️ SecureSight – AI-Powered Safety Vision

**SecureSight** is an AI-powered real-time surveillance system designed to **detect weapons**, **analyze panic situations**, and **send instant alerts** to authorities. Built for **banks, ATMs, and high-security zones**, SecureSight combines **computer vision, AI, and CCTV integration** to enhance security and save lives.

---

## ✨ Features

* 🔫 **Weapon Detection** – Real-time detection of guns, knives, and other threats using AI.
* 😨 **Panic Recognition** – Identifies abnormal or panic behavior in staff/customers.
* 🚨 **Instant Alerts** – Sends notifications to nearby police/security stations automatically.
* 📹 **CCTV Integration** – Works with live CCTV or RTSP streams.
* 📊 **Dashboard (Optional)** – Logs events, detections, and alerts for administrators.
* ⚡ **Offline Support** – Runs locally without cloud dependency for critical security systems.

---

## 🏗️ Tech Stack

* **AI/ML:** PyTorch / TensorFlow, YOLOv8 / custom CNN models
* **Computer Vision:** OpenCV, MediaPipe (for facial/emotion recognition)
* **Backend:** Python (FastAPI / Flask)
* **Notifications:** Twilio / SMTP / Custom Alert System
* **Hardware Integration:** Works with IP cameras / CCTV streams

---

## 📂 Project Structure

```bash
SecureSight-AI-powered-safety-vision/
│── models/                # Pre-trained AI models (YOLO, emotion detection, etc.)
│── src/                   # Source code
│   ├── detection.py       # Weapon detection logic
│   ├── panic.py           # Panic/emotion recognition
│   ├── alerts.py          # Alert/notification system
│   └── main.py            # Entry point
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the Repository**

```bash
git clone https://github.com/Krishkevin12/SecureSight-AI-powered-safety-vision.git
cd SecureSight-AI-powered-safety-vision
```

2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

* **Run on Webcam**

```bash
python src/main.py
```

* **Run with CCTV/RTSP Feed**

```python
cap = cv2.VideoCapture("rtsp://username:password@ip_address:port/stream")
```

---

## 🚨 Alert Workflow

1. Detects weapon or panic situation.
2. Logs the event with timestamp & camera ID.
3. Sends **instant alert** to nearby authorities.

---



## 🚀 Future Enhancements

* ✅ Multi-camera support
* ✅ Integration with police control rooms
* ✅ Cloud dashboard for centralized monitoring

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.



