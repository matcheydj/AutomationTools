import pythoncom
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import sys
import os
import os.path
import re
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import  FileSystemEventHandler
import  shutil

class MyHandler(FileSystemEventHandler):
	def __init__(self,observer,filename):
		self.observer=observer
		self.filename=filename
	
	def on_created(self,event):
		if not event.is_directory and event.src_path.endswith(self.filename):
                  print "file created "+event.src_path
		  new=re.split('[:/\\\]',event.src_path)[-1]
                  while True:
		    try:
#		      shutil.copy2("V:\\\patches\\"+new,"E:\\\CIS") 
                      if os.path.isfile("F:\\"+new):
		        shutil.copy2("\\\\172.29.22.42\\vulnerabilities\\patches\\"+new,"E:\\CIS") 
		    except:
                      print  sys.exc_info()[0]
		      time.sleep(10)
		    else:
	              break
class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def main(self):
      logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
#      path = 'V:\\\patches'
#      path = r"\\172.29.22.42\vulnerabilities\patches"
      path ="\\\\172.29.22.42\\vulnerabilities\\patches" 
      observer = Observer()
      filename="dmg"
      event_handler = MyHandler(observer,filename)
      observer.schedule(event_handler, path, recursive=True)
      observer.start()
      try:
        while True:
          time.sleep(1)
      except KeyboardInterrupt:
          observer.stop()
          observer.join()
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)
