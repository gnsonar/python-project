from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(subject: str, body: str, senders):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    me = "no-reply@nse-scanner.com"
    msg['From'] = me

    # Record the MIME types of both parts - text/plain and text/html.
    # part1 = MIMEText(text, 'plain')
    part2 = MIMEText(body, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    # msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    mail.login('gnsonar@gmail.com', 'gdukyuetfdxsrfvq')
    for to in senders:
        mail.sendmail(me, to, msg.as_string())
    mail.quit()
