from flask import Flask, request
import smtplib

app = Flask(__name__)

# Route to handle alerts
@app.route('/send_alert', methods=['POST'])
def send_alert():
    alert_type = request.json.get('alert_type')
    
    # Send an email alert (you can replace this with any alert system)
    send_email_alert(alert_type)
    
    return {"message": f"Alert sent for {alert_type}"}, 200

def send_email_alert(alert_type):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    
    subject = "Security Alert"
    body = f"An alert has been triggered: {alert_type} detected!"
    
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail('your_email@gmail.com', 'police_station@gmail.com', message)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
