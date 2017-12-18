##import smtplib
import os,sys,re
from email.mime.text import MIMEText
import sqlite3
import urllib
import urllib.request
from bs4 import BeautifulSoup
import datetime

dateT=datetime.date.today().isoformat()

def check():
    products_new={}
    mail_text=""
    camtasiaUrl="https://www.techsmith.com/camtasia-mac-version-history.html"
    local,headers=urllib.request.urlretrieve(camtasiaUrl)
    soup=BeautifulSoup(open(local,'rt',encoding="utf-8"),"html.parser") 
    div=soup.find_all("div")[0].find_all("h3")[0].text
    camtasiaV=div.split(" ")[-1]
    products_new["camtasia"]=camtasiaV

    boxsyncUrl="https://community.box.com/t5/Box-Release-Notes/bg-p/Release-Notes/label-name/box%20sync"
    local,headers=urllib.request.urlretrieve(boxsyncUrl)
    soup=BeautifulSoup(open(local,'rt',encoding="utf-8"),"html.parser") 
    div=soup.find_all("div","lia-message-body")[0].find_all("font")[0].text
    boxsyncV=div.split(" ")[1]
    products_new["box"]=boxsyncV
   

    conn=sqlite3.connect('updates.db')
    c=conn.cursor()
    for i in c.execute("select name from sqlite_master where type='table'").fetchall():
        
        c.execute("select date,ver from "+i[0]+" where date=(select max(date) from "+i[0]+") ")
        
        big_ver=c.fetchone()
        if products_new[i[0]] > big_ver[1]:
            print(c.execute("select date,ver from "+i[0]).fetchall())
            mail_text+=i[0]+":"+big_ver[1]+" "
            print("INSERT INTO "+i[0]+" VALUES (?,?)",(dateT,products_new[i[0]]))
            c.execute("INSERT INTO "+i[0]+" VALUES (?,?)",(dateT,products_new[i[0]]))
            print(c.execute("select date,ver from "+i[0]).fetchall())
    return mail_text

print(check())

##conn=sqlite3.connect('updates.db')
##c=conn.cursor()
######c.execute('''drop table boxsync''')
####c.execute('''CREATE TABLE box
####             (date text, ver text)''')
####
##c.execute("INSERT INTO box VALUES ('2009-05-05','1.54')")
##conn.commit()
###c.execute('''CREATE TABLE boxsync
###             (date text, ver text)''')
####
###c.execute('''drop TABLE updates''')
##c.execute("INSERT INTO boxsync VALUES ('2009-05-05','6.54')")
####
####c.execute("INSERT INTO camtasia VALUES ('2007-01-05','14.34')")
####
####c.execute("INSERT INTO camtasia VALUES ('2002-01-05','10.34')")
####
####c.execute("INSERT INTO camtasia VALUES ('1997-01-05','10.34')")
####conn.commit()
##
##for i in c.execute("select name from sqlite_master where type='table'").fetchall():
###for i in c.execute("select date,ver from camtasia where date=(select max(date) from camtasia) "):
##  print(i)
##  c.execute("select date,ver from "+i[0]+" where date=(select max(date) from "+i[0]+")")
##  print(c.fetchone())
##conn.commit()
##c.execute("select date,ver from  boxsync")
##print(c.fetchall())
####     print(j[1])
##
###for i in c.execute("select * from updates "):
###    print(i)
##conn.close()
##SERVER = "smtp.gmail.com:587"
##FROM = "wangzhaodong8@gmail.com"
##TO = ["zhaodong.wang@ivanti.com"] # must be a list
##
##SUBJECT = "box sync update to 4.0.7791"
##TEXT = "This is a test of emailing through smtp in google."
##
### Prepare actual message
##
##
##
###msg = MIMEText(message,'plain','utf-8')
###msg['Subject'] = Header("box sync update",'utf-8')
###msg['from'] = 'wangzhaodong8@gmail.com'
###msg['to'] = 'zhaodong.wang@ivanti.com'
##msg = "\r\n".join([
##  "From: wangzhaodong8@gmail.com",
##  "To: zhaodong.wang@ivanti.com",
##  "Subject: Just a message",
##  "",
##  """<html>
##  <head></head>
##  <body>
##    <p>Hi!<br>
##       How are you?<br>
##       Here is the <a href="http://www.python.org">link</a> you wanted.
##    </p>
##  </body>
##</html>
##"""
##  ])
##
### Send the mail
##import smtplib
##server = smtplib.SMTP(SERVER)
##server.ehlo()
##server.starttls()
##server.login("wangzhaodong8@gmail.com", "%LANDesk1%")
##server.sendmail(FROM, TO, msg)
##server.quit()
