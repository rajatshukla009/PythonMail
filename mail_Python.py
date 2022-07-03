from tkinter import *
import smtplib

sender = "blahblah@gmail.com"
receiver = "blahblahblah@gmail.com"
password = "******"
subject = "python email test"
body = "wohoo! completed"

message = f"""From:{sender}
To:{receiver}
subject:{subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in .............")
    server.sendmail(sender,receiver,message)
    print("email has been send")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")