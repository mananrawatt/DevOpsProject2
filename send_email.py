import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, subject, message):
    # Your email configurations
    EMAIL_ADDRESS = 'manannaxis@gmail.com'
    EMAIL_PASSWORD = 'lnve crjx yvkk thth'

    # Recipient's email address (website maintainer or owner)
    recipient_email = 'mananrawat788@gmail.com'

    # Construct the message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
