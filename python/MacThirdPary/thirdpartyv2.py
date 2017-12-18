 # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os,sys,glob,re
import os.path
import shutil
import urllib
import urllib.request
import json
from lxml import etree
from copy import deepcopy
import subprocess
from dateutil.parser import parse
import datetime
import socket
import logging
import time
import sqlite3

products_old={}
logging.basicConfig(

    filename = 'F:\\MacThirdPary\\service.log',

    level = logging.DEBUG, 

    format = '[service] %(levelname)-7.7s %(message)s'

)


def db_item_ver(p_new):
    mail_text=""
    conn=sqlite3.connect('updates.db')
    c=conn.cursor()
    for i in c.execute("select name from sqlite_master where type='table'").fetchall():
        c.execute("select date,ver from "+i[0]+" where date=(select max(date) from "+i[0]+") ")
        big_ver=c.fetchone()
        if p_new[i[0]] > big_ver[1]:
            mail_text+="<li>"+i[0]+":"+p_new[i[0]]+"</li>"+" "
            import time
            timestr=time.strftime("%Y-%m-%d",time.localtime())
            c.execute("insert into "+i[0]+"  values (?,?)",(timestr,p_new[i[0]]))
    conn.commit()
    conn.close()
    return " <ul>"+mail_text+" </ul>"

def check():
    products_new={}

    
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
           

    return db_item_ver(products_new)
def sendMail():
    
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    

    

    SERVER = "smtp.gmail.com:587"
    FROM = "wangzhaodong8@gmail.com"
    TO = ["zhaodong.wang@ivanti.com"] # must be a list
    content=MIMEText(check(),'html')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Update Notification"
    msg['From'] ="wangzhaodong8@gmail.com" 
    msg['To'] = "zhaodong.wang@ivanti.com"
    msg.attach(content)

    
    
#    msg = "\r\n".join([
#      "From: wangzhaodong8@gmail.com",
#      "To: zhaodong.wang@ivanti.com",
#      "Subject: Update Notification",
#      "",
#      content.as_string()
#      ])

    # Send the mail
    import smtplib
    server = smtplib.SMTP(SERVER)
    server.ehlo()
    server.starttls()
    server.login("wangzhaodong8@gmail.com", "%LANDesk1%")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
sendMail()
