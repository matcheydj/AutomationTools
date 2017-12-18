from lxml import etree
import os,sys,glob,re,codecs

p=etree.XMLParser(compact=True)
for f in glob.glob('.\\mac\\V[a-zA-Z0-9_-]*.xml'):
  f0=etree.parse(f,parser=p)
  status=f0.xpath("/Vulnerability/Status")[0].text
  if status=="Deleted":
    continue
  desc=f0.xpath("/Vulnerability/Description")[0].text
  vendor=f0.xpath("/Vulnerability/Vendor")[0].text
  flag=0
  if vendor is not None:
    if re.search("LANDESK",vendor) is not None:
      f0.xpath("/Vulnerability/Vendor")[0].text="Ivanti"
      flag=1
  if desc is not None:
    if re.search("LANDESK",desc) is not None:
      f0.xpath("/Vulnerability/Description")[0].text=re.sub("LANDESK","Ivanti",desc).strip()
      flag=1
  print(f)
  if flag==1:
      print(f)
      patch0=f0.xpath("/Vulnerability/Patches/Patch")[0]
##      name=patch0.find("Name")
##      if patch0.find("SupercededBy") is not None:
##        patch0.find("SupercededBy").addnext(name)
      vul=f0.xpath("/Vulnerability")[0]
      patch0.attrib.pop("size",None)
      if len(patch0.xpath("AdditionalFiles")) is not 0:
  
       patch0.remove(patch0.xpath("AdditionalFiles")[0])
      if len(patch0.xpath("Processes")) is not 0:
       patch0.remove(patch0.xpath("Processes")[0])
      if len(vul.xpath("AssociatedProducts")) is not 0:
       vul.remove(vul.xpath("AssociatedProducts")[0])
      if len(vul.xpath("IAVAs")) is not 0:
       vul.remove(vul.xpath("IAVAs")[0])
      group=f0.find("Groups")
      sta=f0.find("Status")
      groupEle=etree.Element("Groups")
      if group is None:
       sta.addnext(groupEle)
      depend=f0.find("DependsOn")
      dependEle=etree.Element("DependsOn")
      g=f0.find("Groups")
      if  depend is None:
       g.addnext(dependEle)
      rev=f0.xpath("/Vulnerability/@Revision")[0]
      rev=int(rev)+1
      f0.xpath("/Vulnerability")[0].set("Revision",str(rev))
      publish=f0.xpath("/Vulnerability/PublishDate")[0].text
      
      if re.search("\+00:00",publish) is not None:
        newPublish=re.sub("\+00:00","",publish)
        f0.xpath("/Vulnerability/PublishDate")[0].text=newPublish
      new=re.sub('.\\\\mac\\\\',"",".\\\\dest\\\\"+f)
      final=re.sub('.\\\\mac\\\\',"",".\\\\final\\\\"+f)
      f0.write(new,encoding="utf8",xml_declaration=True,pretty_print=False)
      with open(new,'r',encoding='utf-8') as f:
        contents=f.read().replace('/>',' />').replace('<?xml version=\'1.0\' encoding=\'UTF8\'?>','<?xml version="1.0"?>').replace('+00:00','').replace("><",">\n  <").replace("xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"","xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"")
        
        with open(final,'w',encoding='utf-8') as fi:
          fi.write(contents)
        
