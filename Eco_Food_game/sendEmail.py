import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Reading from the config file and assigning the config variable
with open('config.json') as f:
    config = json.load(f)

smtp = config['smtpServer']
email = config['email']
emailPassword = config['emailPassword']


def send(recipient, message):
    """
    Sends an email to the recipient with the passed message
    :param recipient: The email-address that will receive the email message
    :param message: The message that will be sent
    """
    # Create a message object
    msg = MIMEMultipart()

    # Set the sender, recipient, and subject
    msg['From'] = email
    msg['To'] = recipient
    msg['Subject'] = 'Eco Test Game'

    # Add the message body
    body = message
    msg.attach(MIMEText(body, 'plain'))

    # Create an SMTP connection and send the message
    with smtplib.SMTP(smtp, 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, emailPassword)
        smtp.send_message(msg)
