import os,re,sys
from lxml import etree
import glob

for i in glob.glob("*.xml");
 f=etree.parse(i)
 title=f.xpath("/Vulnerability/Title")[0].text
 print(title) 
