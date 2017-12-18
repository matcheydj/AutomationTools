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
	
#	def check(self,f):
#		while True:
#		  try:
#		    shutil.copy2("F:\\"+f,"E:\\CIS") 
#		  except:
#                    print  sys.exc_info()[0]
#		    time.sleep(10)
#		  else:
#	            break
#		a=os.stat(f).st_atime
#		b=os.stat(f).st_ctime
#		print a
#		print b
#		time.sleep(3)
#		if a!=b:
#			return True
#		else:
#			return False
	def on_created(self,event):
		if not event.is_directory and event.src_path.endswith(self.filename):
                  print "file created "+event.src_path
		  new=re.split('[:/\\\]',event.src_path)[-1]
                  while True:
		    try:
#		      shutil.copy2("F:\\"+new,"E:\\CIS") 
		      shutil.copy2("\\\\172.29.22.42\\vulnerabilities\\patches\\"+new,"\\\\172.29.0.154\\MacPatches") 
		    except:
                      print  sys.exc_info()[0]
		      time.sleep(10)
		    else:
	              break
	def on_modified(self,event):
		print "hello world"
		if not event.is_directory and event.src_path.endswith("xml"):
                  print "file modified"+event.src_path
		  new=re.split('[:/\\\]',event.src_path)[-1]
                  while True:
		    try:
			    shutil.copy2("F:\\scripts\\python\\"+new,"\\\\bej-data001\\Patch-Mac\\rhel7_security") 
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
