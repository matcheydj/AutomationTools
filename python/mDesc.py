from lxml import etree
import os,sys,glob,re,codecs

p=etree.XMLParser(compact=False)
f0=etree.parse("V_INTL_Adobe-PhotoShop-CS6-Update-1304_Manual.xml",parser=p)
date=f0.find("Groups")
sta=f0.find("Status")
group=etree.Element("Groups").tag
if date is None:
    sta.addnext(group)
d=f0.find("DependsOn")
depend=etree.Element("DependsOn")
g=f0.find("Groups")
if  d is None:
    g.addnext(depend)
vendor=f0.find("Groups")
f0.find("Status").addnext(vendor)


f0.write("test.xml",pretty_print=True)

with open("test.xml","r",encoding="utf-8") as t:
    contents=t.read().replace("><",">\n  <")

    with open("test.xml","w",encoding="utf-8") as f:
        f.write(contents)
#      if re.search("\+00:00",publish) is not None:
#        newPublish=re.sub("\+00:00","",publish)
#        f0.xpath("/Vulnerability/PublishDate")[0].text=newPublish
#      new=re.sub('.\\\\mac\\\\',"",".\\\\dest\\\\"+f)
#      final=re.sub('.\\\\mac\\\\',"",".\\\\final\\\\"+f)
#      f0.write(new,encoding="utf8",xml_declaration=True,pretty_print=False)
#      with open(new,'r',encoding='utf-8') as f:
#        contents=f.read().replace('/>',' />').replace('<?xml version=\'1.0\' encoding=\'UTF8\'?>','<?xml version="1.0"?>')
#        
#        with open(final,'w',encoding='utf-8') as fi:
#          fi.write(contents)
#        
