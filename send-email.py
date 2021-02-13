# To be possible to send email from gmail, enable the less secure apps:
# https://www.google.com/settings/security/lesssecureapps

import smtplib
import ssl

smtp_server = 'smtp.gmail.com'
port = 587  # For starttls
sender_email = "douglasfornaro@gmail.com"
password = input('Enter your password: ')

receiver_email = "douglasfornaro@hotmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()

server = smtplib.SMTP(smtp_server, port)
try:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()
