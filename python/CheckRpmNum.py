import os
import sys
import urllib
from bs4 import BeautifulSoup
import re
from lxml  import etree
import glob

def findRPMs(url):
    page=urllib.urlopen(url)
    soup=BeautifulSoup(page)
    pre=soup.find_all('pre')
    text=pre[0] 
    gs=re.findall(r"([a-zA-Z0-9+._-]+[0-9].rpm)",str(text))
    gs.sort()
    return gs


def  findContents(f):
	bs=etree.parse(f)
	patch=bs.xpath('//@UniqueFilename')
	n=[]
	for i in patch:
	     n.append(re.sub('\\*',"",i))
        n.sort()
	return n
fs=glob.glob("V_INTL*")
for f in fs:
   temp=etree.parse(f)
   url=temp.xpath('/Vulnerability/MoreInfoURL')[0].text
   rpms=findRPMs(url)
   items=findContents(f) 
   for a in rpms:
       if a not in items:
           print "%s    " %f
           print "%s    " %a
	   break
