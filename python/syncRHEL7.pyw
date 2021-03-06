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
	
	def on_modified(self,event):
		if not event.is_directory and event.src_path.endswith(self.filename):
                  print "file modified"+event.src_path
		  new=re.split('[:/\\\]',event.src_path)[-1]
                  while True:
		    try:
#			    if (os.path.isfile("\\\\bej-data001\\Patch-Mac\\rhel7_security"+new)):
#				    os.remove("\\\\bej-data001\\Patch-Mac\\rhel7_security"+new)
#			    shutil.copy2("E:\\scripts\\python\\"+new,"\\\\bej-data001\\Patch-Mac\\rhel7_security") 
			    if (os.path.isfile("\\\\172.29.22.42\\vulnerabilities\\redhat_security"+new)):
				    os.remove("\\\\172.29.22.42\\vulnerabilities\\redhat_security"+new)
			    shutil.copy2("E:\\scripts\\python\\"+new,"\\\\172.29.22.42\\vulnerabilities\\redhat_security") 
		    except:
                      print  sys.exc_info()[0]
		      time.sleep(10)
		    else:
	              break
#                  self.check("F:/"+new)
#		  ctime=os.stat("F:\\"+new).st_mtime
#		  while True:
#			  if(self.check("F:\\"+new)):
#		               shutil.copy2("F:\\"+new,"E:\\CIS")
#			       print "copying done"
#			       break
#		          time.sleep(2)
			  
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
#    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path ="E:\\scripts\\python"
    observer = Observer()
    filename="xml"
    event_handler = MyHandler(observer,filename)
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
