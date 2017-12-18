import smtplib

FROMADDR = "zhaodong.wang@landesk.com"
LOGIN    = "ld\zwang"
PASSWORD = "%LANDesk1%"
TOADDRS  = ["zhaodong.wang@landesk.com"]
SUBJECT  = "Test"

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
msg += "some text\r\n"

server = smtplib.SMTP('smtp.office365.com', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()

