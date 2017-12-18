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
import win32serviceutil
import win32service
import win32event
import servicemanager
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
    if not os.path.exists('F:\\MacThirdPary\\updates.db.bak'):
        shutil.copy2('F:\\MacThirdPary\\updates.db','F:\\MacThirdPary\\updates.db.bak')
    mail_text=""
    conn=sqlite3.connect('updates.db')
    c=conn.cursor()
    for i in c.execute("select name from sqlite_master where type='table'").fetchall():
        c.execute("select date,ver from "+i[0]+" where date=(select max(date) from "+i[0]+") ")
        big_ver=c.fetchone()
        if p_new[i[0]] > big_ver[1]:
            mail_text+=i[0]+":"+big_ver[1]+" "
           
    conn.close()
    return mail_text
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

    SERVER = "smtp.gmail.com:587"
    FROM = "wangzhaodong8@gmail.com"
    TO = ["zhaodong.wang@ivanti.com"] # must be a list
    content=check()
    
    msg = "\r\n".join([
      "From: wangzhaodong8@gmail.com",
      "To: zhaodong.wang@ivanti.com",
      "Subject: Update Notification",
      "",
      content
      ])

    # Send the mail
    import smtplib
    server = smtplib.SMTP(SERVER)
    server.ehlo()
    server.starttls()
    server.login("wangzhaodong8@gmail.com", "%LANDesk1%")
    server.sendmail(FROM, TO, msg)
    server.quit()

class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "UpdateService"
    _svc_display_name_ = "Update Service"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)

        self.stop_event = win32event.CreateEvent(None,0,0,None)

        socket.setdefaulttimeout(60)

        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)

        win32event.SetEvent(self.stop_event)

        logging.info('Stopping service ...')

        self.stop_requested = True
    def SvcDoRun(self):
        servicemanager.LogMsg(

            servicemanager.EVENTLOG_INFORMATION_TYPE,

            servicemanager.PYS_SERVICE_STARTED,

            (self._svc_name_,'')

        )

        self.main()

    def main(self):
        logging.info(' ** PyWin32 service  ** ')
        while True:
            if self.stop_requested:
                break
            time.sleep(18000)
            sendMail()
            


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
