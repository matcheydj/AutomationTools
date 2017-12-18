import smtplib
import os,sys,re
from email.mime.text import MIMEText

SERVER = "smtp.gmail.com:587"
FROM = "wangzhaodong8@gmail.com"
TO = ["zhaodong.wang@ivanti.com"] # must be a list

SUBJECT = "box sync update to 4.0.7791"
TEXT = "This is a test of emailing through smtp in google."

# Prepare actual message



#msg = MIMEText(message,'plain','utf-8')
#msg['Subject'] = Header("box sync update",'utf-8')
#msg['from'] = 'wangzhaodong8@gmail.com'
#msg['to'] = 'zhaodong.wang@ivanti.com'
msg = "\r\n".join([
  "From: wangzhaodong8@gmail.com",
  "To: zhaodong.wang@ivanti.com",
  "Subject: Just a message",
  "",
  """<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""
  ])

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.ehlo()
server.starttls()
server.login("wangzhaodong8@gmail.com", "%LANDesk1%")
server.sendmail(FROM, TO, msg)
server.quit()
