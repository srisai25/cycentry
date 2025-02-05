import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_feedback(feedback_text,receiver_email):
    # Email configuration
    sender_email = 'kmitgotnochill@gmail.com'#enter your email
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # You might need to change this based on your SMTP server configuration
    smtp_username = 'kmitgotnochill@gmail.com'#enter your email
    smtp_password = 'zgprrtpfydxretwh'

    # Create a MIMEText object with the feedback text
    msg = MIMEMultipart()

    # Set the sender and recipient email addresses
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'We have received your valuable feedback.'

    body = f"""
    <p>Dear User,</p>
    <p>We have recieved your valuable feedback.</p>
    <p>Feedback given : "{feedback_text}"</p>
    <p>Thank you for providing feedback, it helps us improve.</p>
    <p>Best regards,</p>
    <p>Cysentry Team</p>
    """
    msg.attach(MIMEText(body, 'html'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use TLS for secure connection
    server.login(smtp_username, smtp_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Disconnect from the SMTP server
    server.quit()

def email_feedback(feedback,user_email):
    print(feedback)
    with open('feedback.txt', 'a') as f:
        f.write(feedback + '\n')
    send_feedback(feedback,user_email)
    print("Feedback sent successfully!")