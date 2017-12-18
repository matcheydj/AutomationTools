import os
import re
import time
import datetime
import string
from lxml import etree

def compare(a):
        
        return a.replace("-","")
f=etree.parse('F:\correctXML\V_ENU_OFFICE-2011-1423.xml')
list=f.xpath("/Vulnerability/PublishDate")
t="2011-02-00"
filet=""
#r=re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
for a in list:
	a=re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}',a.text)
	filet=a[0]

#ft=os.path.getmtime("txt")
#print datetime.datetime.fromtimestamp(ft)
if compare(t) > compare(filet):
        print filet + " time"
