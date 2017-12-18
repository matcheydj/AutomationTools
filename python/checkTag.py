from lxml import etree
import os,sys,glob,re
import shutil

for f in glob.glob('E:\\mac\\V_[Va-zA-Z0-9_-]*.xml'):
  f0=etree.parse(f)
#  state=f0.xpath("/Vulnerability/Status")[0].text
#  exist=f0.findall("//URL")
#  if re.search("GoogleChrome",f):
#    continue
#  if state=="Deleted": 
#    continue
#  if len(exist)==0:
#    continue
#    
  try:
#      type=f0.xpath("/Vulnerability/Patches/Patch")[0].xpath("Remediation/RepairType")[0].text
      type=f0.xpath("//Vulnerability/Patches/Patch")
      if (len(type) > 1):
	      print f+" : "+str(len(type))
  except Exception:
      pass
#    if re.match("^\*",uniquename):
#      continue
##    url=f0.xpath("/Vulnerability/Patches/Patch")[0].("URL")
#    url=f0.xpath("/Vulnerability/Patches/Patch")[0].xpath("URL")
#    if len(url)!=0:
#      if uniquename!="" and download=="DManual" and re.match("^http",str(url[0].text)):
#        shutil.copy2(f,"E:\\tmp\\") 
#  except KeyError:
#      shutil.copy2(f,"E:\\tmp\\") 
for i in range(2):
  print i
