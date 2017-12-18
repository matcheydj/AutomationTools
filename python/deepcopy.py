from lxml import etree
import os,sys,glob,re
import shutil
from copy import deepcopy

from bs4 import BeautifulSoup


def replace_with_newlines(element):
    text = ''
    for elem in element.recursiveChildGenerator():
        if isinstance(elem, str):
            text += elem.strip()
            
##            print("text is "+elem)
        elif elem.name == 'br':
            print("element is "+elem.text)
            text += '\n'
    return text

page = """<html>
<body>
<p>America,<br>
Now is the<br>time for all good men to come to the aid<br>of their country.</p>
<p>pile on taxpayer debt<br></p>
<p>Now is the<br>time for all good men to come to the aid<br>of their country.</p>
</body>
</html>
"""

soup = BeautifulSoup(page,"html.parser")
lines = soup.find("body")
for line in lines.findAll('p'):
    line = replace_with_newlines(line)
    

##f0=etree.parse("template.xml")
##patch=f0.xpath("/Vulnerability/Patches/Patch")[0]
##patch2=deepcopy(patch)
##patch3=deepcopy(patch)
##patch.getparent().append(patch2)
##patch.getparent().append(patch3)
##V=f0.xpath("/Vulnerability/Patches/Patch/Cmds/Cmd/Args/Arg")[0].get("V")
##f0.xpath("/Vulnerability/Patches/Patch/Cmds/Cmd/Args/Arg")[0].set("V",V.replace("template","GDB"))
##f0.write("2.xml")
##name="thunderbird-45.8.0-1.el6_8.x86_64.rpm"

##def parserpm(rpmname):
##    rpmlist=rpmname.strip("x86_64.rpm").split("-")
##    rname=""
##    rversion=""
##    for i in rpmlist:
##        if "." not in i:
##            
##            rname=rname+"-"+i
##        if "." in i:
##            rversion=rpmlist[rpmlist.index(i):]
##            break
##            
##    print(rname)
##    print(rversion)
##    r1=rname.strip("-")
##    r2="-".join(rversion)
##    return [r1,r2]
##
##print(parserpm(name)) 
