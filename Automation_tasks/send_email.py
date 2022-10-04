from inspect import _SourceObjectType
import smtplib
import ssl # to connect to a gmail account
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python"
sender_email = "coderacerlivestreamapp@gmail.com"
receiver_email = "coderacerlivestreamapp@gmail.com"
password = input("Enter a password: ")

#build the email

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

html = f""" # multiline f string
<html>
    <body>
        <h1>{subject}<¨/h1>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype ="html")

context = ssl.create_default_context() # give context for sending secure email

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context =context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string)
print("Success")

