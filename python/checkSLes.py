from lxml import etree
import os,sys,glob,re
import shutil
import xlwt

root=etree.Element('Root')
doc=etree.ElementTree(root)
wb=xlwt.Workbook()
centos5s=wb.add_sheet("cenots5")
centos6s=wb.add_sheet("cenots6")
centos7s=wb.add_sheet("cenots7")
centos5_x86_64s=wb.add_sheet("cenots5_x86_64")
centos6_x86_64s=wb.add_sheet("cenots6_x86_64")
centos7_x86_64s=wb.add_sheet("cenots7_x86_64")
datere=re.compile("....-..-..")
j=0
k=0
l=0
m=0
n=0
r=0
for f in glob.glob('E:\\tmp\\sles9\\V_[Va-zA-Z0-9_-]*.xml'):
 f0=etree.parse(f)
 state=f0.xpath("/Vulnerability/Status")[0].text
 if state=="Deleted": 
    continue
  exist=f0.findall("//URL")
  if re.search("GoogleChrome",f):
    continue
  if state=="Deleted": 
    continue
  if len(exist)==0:
    continue
    
  try:
    uniquename=f0.xpath("/Vulnerability/Patches/Patch")[0].attrib['UniqueFilename']
    try:
      download=f0.xpath("/Vulnerability/Patches/Patch")[0].attrib['Download']
    except KeyError:
      continue
    if re.match("^\*",uniquename):
      continue
    url=f0.xpath("/Vulnerability/Patches/Patch")[0].("URL")
    url=f0.xpath("/Vulnerability/Patches/Patch")[0].xpath("URL")
    if len(url)!=0:
      if uniquename!="" and download=="DManual" and re.match("^http",str(url[0].text)):
        shutil.copy2(f,"E:\\tmp\\") 
  except KeyError:
      shutil.copy2(f,"E:\\tmp\\") 
 centos5=""
 centos5_x86_64=""
 centos6=""
 centos6_x86_64=""
 centos7=""
 centos7_x86_64=""
 publish=""
 type=f0.xpath("//Vulnerability/Patches/Patch")
 type_len=len(type)
 for i in range(type_len):
  try:
     V=f0.xpath("/Vulnerability/Patches/Patch")[i].xpath("Cmds/Cmd/Args/Arg")[0].attrib['V']
     
     IDS=f0.xpath("/Vulnerability/Patches/Patch")[i].xpath("//Platforms/ID")
     for i in IDS:
       i=i.text
       if i=="centos5":
         centos5=i
       if i=="centos6":
         centos6=i
       if i=="centos7":
         centos7=i
       if i=="centos5_x86_64":
         centos5_x86_64=i
       if i=="centos6_x86_64":
         centos6_x86_64=i
       if i=="centos7_x86_64":
         centos7_x86_64=i
     publish=f0.xpath("/Vulnerability/PublishDate")[0].text
     publish=datere.match(publish).group()
  except:
     pass
    print f
    break
 if centos5!="":
   centos5s.write(j,0,f)
   centos5s.write(j,1,publish)
   j+=1
 if centos6!="":
   centos6s.write(k,0,f)
   centos6s.write(k,1,publish)
   k+=1
 if centos7!="":
   centos7s.write(l,0,f)
   centos7s.write(l,1,publish)
   l+=1
 if centos5_x86_64!="":
   centos5_x86_64s.write(m,0,f)
   centos5_x86_64s.write(m,1,publish)
   m+=1
 if centos6_x86_64!="":
   centos6_x86_64s.write(n,0,f)
   centos6_x86_64s.write(n,1,publish)
   n+=1
 if centos7_x86_64!="":
   centos7_x86_64s.write(r,0,f)
   centos7_x86_64s.write(r,1,publish)
   r+=1
wb.save("centos_stat.xls")
