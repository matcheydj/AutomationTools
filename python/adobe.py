import os,sys,re
import urllib.request
from bs4 import BeautifulSoup
import datetime
from lxml import etree

##flashurl="http://www.adobe.com/support/security/bulletins/apsb11-28.html"
##flashRes=urllib.request.urlopen(flashurl)
##flash=BeautifulSoup(flashRes,"html.parser")
##body=flash.find_all(id="L0C1-body")[0]
##flashDate=body.find_all("p")[0]
##flashCVE=body.find_all("p")[2]
##flashD=datetime.datetime.strptime(flashDate.text.split(":")[1]," %B %d, %Y")
##flashD2=flashD.strftime("%Y-%m-%d")
##
##flashCVEs=flashCVE.text.split(":")[1].replace(" ","")
##flashVersion=flash.find_all("table")[-1].find_all("tr")[1].find_all("td")[1]
##print(flashVersion.text)
##flashDetail=flash.find_all("div",id="L0C1")[0].find_all("h3")[4]
##desc=[]
##for i in flashDetail.find_next_siblings("p"):
##  if i.string==None:
##    continue
##  desc.append(i.string)
##flashDesc="\n".join(desc)
##


##Mac flash player
lines=[]
with open("D:/source.txt") as src:
    lines=src.readlines()
date=lines[0].split(":")[1]
flashD=datetime.datetime.strptime(date[:-1],"%B %d, %Y")
flashD2=flashD.strftime("%Y-%m-%d")
flasholdversion=lines[1].split(":")[1][:-1]
flashVersion=lines[2].split(":")[1][:-1]
url=lines[3].split(":")[1:]
flashurl=":".join(url)[:-1]
flashDesc=lines[4].split(":")[1]
cve=[]
for i in lines[5:]:
  if re.match("CVE-[0-9]{4}-[0-9]{4,}",i):
      cve.append(i[:-1])
      
flashCVEs=",".join(cve)
vul_id="AdobeFlashPlayer"+flashVersion+"_Detect_Only"

flashF=etree.parse("v:\mac\V_INTL_AdobeFlashPlayer"+flasholdversion+"_Detect_Only.xml")
flashF.xpath("/Vulnerability")[0].set("Vul_ID",vul_id)
flashF.xpath("/Vulnerability")[0].set("CVE_ID",flashCVEs)
flashF.xpath("/Vulnerability/Patches/Patch/Files/File/Version")[0].text=flashVersion
flashF.xpath("/Vulnerability/Patches/Patch/Name")[0].text="Adobe Flash Player "+flashVersion+" update"
flashF.xpath("/Vulnerability/Description")[0].text=flashDesc
flashF.xpath("/Vulnerability/MoreInfoURL")[0].text=flashurl
flashF.xpath("/Vulnerability/PublishDate")[0].text=flashD2+"T00:00:00.0000000"
flashF.xpath("/Vulnerability/Title")[0].text="Adobe Flash Player ("+flashVersion+")"  
f="V_INTL_"+vul_id+".xml"
flashF.write("D:/"+f)

##Linux 32bit flash player
flash32=etree.parse("v:\CentOS\V_INTL_flash-player-npapi-"+flasholdversion+".xml")
#flash32.xpath("/Vulnerability/Status")[0].text="Enabled"
flashvul_id="flash-player-npapi-"+flashVersion
flashunique="flash-player-npapi-"+flashVersion+"-release.i386.rpm"
flash32.xpath("/Vulnerability")[0].set("Vul_ID",flashvul_id)
flash32.xpath("/Vulnerability")[0].set("CVE_ID",flashCVEs)
flash32.xpath("/Vulnerability/Patches/Patch")[0].set("UniqueFilename","*"+flashunique)
flash32.xpath("/Vulnerability/Patches/Patch/Files/File/Version")[0].text=flashVersion+"-release"
flash32.xpath("/Vulnerability/Patches/Patch/Name")[0].text=flashunique
flash32.xpath("/Vulnerability/Description")[0].text=flashDesc
flash32.xpath("/Vulnerability/MoreInfoURL")[0].text=flashurl
flash32.xpath("/Vulnerability/PublishDate")[0].text=flashD2+"T00:00:00.0000000"
flash32.xpath("/Vulnerability/Title")[0].text="Adobe Flash Player ("+flashVersion+")"  
f32="V_INTL_"+flashvul_id+".xml"
flash32.write("D:/"+f32)


##Linux 64bit flash player
flash64=etree.parse("v:\CentOS\V_INTL_flash-player-npapi-"+flasholdversion+"_DetectOnly.xml")
#flash64.xpath("/Vulnerability/Status")[0].text="Enabled"
flashvul_id="flash-player-npapi-"+flashVersion+"_DetectOnly"
flashunique="flash-player-npapi-"+flashVersion+"-release.x86_64.rpm"
flash64.xpath("/Vulnerability")[0].set("Vul_ID",flashvul_id)
flash64.xpath("/Vulnerability")[0].set("CVE_ID",flashCVEs)
flash64.xpath("/Vulnerability/Patches/Patch/Files/File/Version")[0].text=flashVersion+"-release"
flash64.xpath("/Vulnerability/Patches/Patch/Name")[0].text=flashunique
flash64.xpath("/Vulnerability/Description")[0].text=flashDesc
flash64.xpath("/Vulnerability/MoreInfoURL")[0].text=flashurl
flash64.xpath("/Vulnerability/PublishDate")[0].text=flashD2+"T00:00:00.0000000"
flash64.xpath("/Vulnerability/Title")[0].text="Adobe Flash Player ("+flashVersion+")"  
f64="V_INTL_"+flashvul_id+".xml"
flash64.write("D:/"+f64)

##response=urllib.request.urlopen("https://helpx.adobe.com/security/products/acrobat/apsb17-36.html")
##soup=BeautifulSoup(response,"html.parser")
##date=soup.find_all(class_="table parbase section")[0].find_all("td")[1].text
##d=datetime.datetime.strptime(date,"%B %d, %Y")
##print(d.strftime("%Y-%m-%d"))
##print(soup.find_all(class_="text")[0].find("p").text)
##cves=soup.find_all(class_="table parbase section")[3].text
##print(",".join(re.findall("CVE-[0-9]+-[0-9]+",cves)))
##versions=soup.find_all(class_="table parbase section")[2]
##for i in versions.find_all("tr")[1:]:
##  if i.find_all("td")[0].text=="Acrobat XI":
##    print(i.find_all("td")[1].text)
