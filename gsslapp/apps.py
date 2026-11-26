from flask import Flask, render_template, request
from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Route to show the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Route that handles the form submission when "Send Message" is clicked
@app.route('/send', methods=['POST'])
def send_email():
    # Get form data from the HTML inputs
    name = request.form.get('user_name')
    user_email = request.form.get('user_email')
    message_content = request.form.get('message')

    # Your email configuration (e.g., Gmail)
    sender_email = "your_email@gmail.com"
    sender_password = "your_gmail_app_password" # Use a Google App Password, not your real password
    receiver_email = "your_email@gmail.com" # Where you want to receive the message

    # Construct the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"New Contact Form Message from {name}"
    
    body = f"Name: {name}\nEmail: {user_email}\n\nMessage:\n{message_content}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server securely
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return "<h3>Success! Your email was sent via Python.</h3><a href='/'>Go back</a>"
    except Exception as e:
        return f"<h3>Failed to send email:</h3> <p>{e}</p><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(debug=True)