 # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os,sys,glob,re
import shutil
import urllib
import urllib.request
import json
from lxml import etree
from copy import deepcopy
import types


def parserpm(rpmname):
    rpmnameN=".".join(rpmname.split(".")[:-2])
    rpmlist=rpmnameN.split("-")
    rname=""
    rversion=""
    r2="-".join(rpmlist[-2:])
    r1="-".join(rpmlist[:-2])
    return [r1,r2]

def replace_with_newlines(element):
    text = ''
    for elem in element.recursiveChildGenerator():
        if isinstance(elem, str):
            text += elem.strip()
        elif elem.name == 'br':
            text += '\n'
    return text


local,headers=urllib.request.urlretrieve("https://rhn.redhat.com/errata/rhel-server-6-errata-security.html")

soup=BeautifulSoup(open(local,'rt',encoding="utf-8"),"html.parser")     

table=soup.find_all("script")


s1=re.sub("^.*\[\[","\[\[",str(table[5].contents))
s2=re.sub("\]\].*$","\]\]",s1)
for i in s2.split("],["):
    fields=i.replace("\\\'","").split(",")
    vul=fields[2].replace(":","-")
    vlocal,vheaders=urllib.request.urlretrieve("https://rhn.redhat.com/errata/"+vul+".html")

    vsoup=BeautifulSoup(open(vlocal,'rt',encoding="utf-8"),"html.parser")
    print(vul)
    vheader=vsoup.find_all("h1")[1].text
   
    vdiv=vsoup.find("div","page-summary")
    for line in vdiv.findAll('p'):
      line = replace_with_newlines(line)
    
    vpublish=vsoup.find("table","details").find_all("tr")[3].find("td").text
    vcve=vsoup.find("table","details").find_all("tr")
    cves=""
    if len(vcve) == 7:
      vall=vcve[6].find("td").find_all("a")
    
      for cve in vall:
        cves=cves+","+cve.text
    print(cves.strip(","))
    print(vheader)
    print(vpublish)
    print(line)
    vtable=vsoup.find_all("table")
    vtr=vtable[1].find_all("tr")
    flag=0
    x64=0

    template=etree.parse("template.xml")
    patch=template.xpath("/Vulnerability/Patches/Patch")[0]
    template.xpath("/Vulnerability/PublishDate")[0].text=vpublish
    template.xpath("/Vulnerability/Title")[0].text=vheader
    template.xpath("/Vulnerability/Description")[0].text=line
    template.xpath("/Vulnerability/MoreInfoURL")[0].text="https://rhn.redhat.com/errata/"+vul+".html"
    template.xpath("/Vulnerability")[0].set("Vul_ID",vul)
    template.xpath("/Vulnerability")[0].set("CVE_ID",cves.strip(","))
    V=template.xpath("/Vulnerability/Patches/Patch/Cmds/Cmd/Args/Arg")[0].get("V")
    
    vpatch=0
    for i in vtr:
        if re.search("Red Hat Enterprise Linux Server",str(i.contents)):
            flag=1
            continue
        if flag is 1:
            if  re.search("x86_64:",str(i.contents)):
                x64=1
                continue
        if flag is 1 and x64 is 1:
                print(i.find("td").text.splitlines()[0])
                vname=i.find("td").text.splitlines()[0]
                
                if not re.search("rpm",str(i.find("td").text)):
                    flag=0;x64=0;vname="";vpatch=0
                    break
                if vpatch!=0:
                    
                 tmp=deepcopy(patch)
                 tmp.set("UniqueFilename",vname)
                 tmp.xpath("Name")[0].text=vname
                 tmp.xpath("Files/File/Path")[0].text=parserpm(vname)[0]+"::"+vname.split(".")[-2]
                 tmp.xpath("Files/File/Checksum")[0].text=i.find_all("td")[1].text.split(":")[1].replace("SHA-256","").strip()
                 tmp.xpath("Files/File/Version")[0].text=parserpm(vname)[1]
                 tmp.xpath("Cmds/Cmd/Args/Arg")[0].set("V",V.replace("template",parserpm(vname)[0]))
                 patch.getparent().append(tmp)
                else:
                 patch.set("UniqueFilename",vname)
                 patch.xpath("Name")[0].text=vname
                 patch.xpath("Files/File/Path")[0].text=parserpm(vname)[0]+"::"+vname.split(".")[-2]
                 patch.xpath("Files/File/Checksum")[0].text=i.find_all("td")[1].text.split(":")[1].replace("SHA-256","").strip()
                 patch.xpath("Files/File/Version")[0].text=parserpm(vname)[1]
                 patch.xpath("Cmds/Cmd/Args/Arg")[0].set("V",V.replace("template",parserpm(vname)[0]))
                vpatch=vpatch+1
                print(vpatch)

                

    
    template.write("V_INTL_"+vul+".xml")
   
