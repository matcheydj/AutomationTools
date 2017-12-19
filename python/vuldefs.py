from lxml import etree
import os,sys,glob,re,codecs
from copy import deepcopy
from subprocess import call
import argparse
from shutil import copy


oldpwd=os.getcwd()
print oldpwd
parser=argparse.ArgumentParser(description='test')
parser.add_argument('--contents_dir',help="this is the directory of contents.")
parser.add_argument('--prod_path',help="this is the directory of products.")
args=parser.parse_args()
contents_dir=args.contents_dir
#for v in glob.glob('./V[a-zA-Z0-9_-]*.xml'):
#	fxml=etree.parse(v)
#	pids=fxml.xpath("//Products/ID")
#	
#	for i in pids:
#           if os.path.isfile("P_"+i.text+".xml"):
#                   print(i.text+"   exists")
#           else:
#                   if args.prod_path is not None:
#                           copy(args.prod_path+"P_"+i.text+".xml",os.getcwd()) 
#			   
#
xmlparser=etree.XMLParser(encoding='utf-8')
template=etree.parse("vul.xml",xmlparser)
vulEle=template.xpath("/GetVulnerabilitiesOfTypeResult/vulnerabilities/vulnerability")[0]
vulEleBak=deepcopy(vulEle)
vul_flag=0
for f in glob.glob(contents_dir+'/V[a-zA-Z0-9_-]*.xml'):
  f0=etree.parse(f)
  status=f0.xpath("/Vulnerability/Status")[0].text
  if status=="Deleted":
    continue
  vul=vulEle
  if vul_flag>0:
    vul=deepcopy(vulEleBak)
  vul_flag+=1
  vul.set("Vul_ID",f0.xpath("@Vul_ID")[0])
  vul.set("CVE_ID",f0.xpath("@CVE_ID")[0])
  vulEle.getparent().append(vul)
  desc=f0.xpath("/Vulnerability/Description")[0].text
  vul.xpath("Title")[0].text=f0.xpath("/Vulnerability/Title")[0].text
  patches=f0.xpath("/Vulnerability/Patches/Patch")
  flag=0
  patchEle=vul.xpath("Patches/Patch")[0]
  for p in patches:
          element=patchEle
          if flag >0:
            element=deepcopy(patchEle)
          element.xpath("Name")[0].text=p.xpath("@UniqueFilename")[0]
          element.set("UniqueFilename",p.xpath("@UniqueFilename")[0])
          element.xpath("Files/File/Path")[0].text=p.xpath("Files/File/Path")[0].text
          element.xpath("Files/File/Checksum")[0].text=p.xpath("Files/File/Checksum")[0].text
          element.xpath("Files/File/Version")[0].text=p.xpath("Files/File/Version")[0].text
          prodIDs=p.xpath("Products/ID")
          ProdEle=element.xpath("Products/ID")[0]
          ProdEleBak=deepcopy(ProdEle)
          prod_flag=0
          for prodID in prodIDs:
            prod=ProdEle
            if prod_flag >0:
               prod=deepcopy(ProdEleBak)
               prod_flag+=1
            prod.text=prodID.text
          element.xpath("Cmds/Cmd/Args/Arg")[0].set("V",p.xpath("Cmds/Cmd/Args/Arg/@V")[0].replace("\n","&#xA;").replace("\r","").replace("&>","&gt;&amp;").replace("\"","&quot;"))
          patchEle.getparent().append(element)
          flag+=1


prodEle=template.xpath("/GetVulnerabilitiesOfTypeResult/products/prod")[0]
prodEleBak=deepcopy(prodEle)
prod_flag=0
#for p in glob.glob('./linux/P[a-zA-Z0-9_-]*.xml'):
for v2 in glob.glob(contents_dir+'/V[a-zA-Z0-9_-]*.xml'):
  v2xml=etree.parse(v2)
  p2ids=v2xml.xpath("//Products/ID")
  for i2 in p2ids:
   p0=etree.parse(contents_dir+"/P_"+i2.text+".xml")
   prod=prodEle
   if prod_flag>0:
     prod=deepcopy(prodEleBak)
   prod_flag+=1
   prod.set("Prod_ID",p0.xpath("@Prod_ID")[0])
   prod.xpath("Name")[0].text=p0.xpath("/PatchProductXML/Name")[0].text
   prod.xpath("DetectedByRPMs/RPM/filename")[0].text=p0.xpath("/PatchProductXML/DetectedByRPMs/RPM/filename")[0].text
   prod.xpath("DetectedByRPMs/RPM/minVersion")[0].text=p0.xpath("/PatchProductXML/DetectedByRPMs/RPM/minVersion")[0].text
   prod.xpath("DetectedByRPMs/RPM/maxVersion")[0].text=p0.xpath("/PatchProductXML/DetectedByRPMs/RPM/maxVersion")[0].text
   prodEle.getparent().append(prod)
  
  
template.write(oldpwd+"/temp.xml")


from subprocess import call
import time
detectedV=[]
detectedNew=open("detectedN","w")
os.chdir("/opt/landesk/bin/")
call(["./vulscan","-d",oldpwd+"/temp.xml","-o","out"])
while not os.path.isfile("out"):
   time.sleep(3) 
with open("/opt/landesk/bin/out") as detected:
  f_flag=0
  for line in detected:
    if re.search("<results",line):
      f_flag=1 
    if re.search("</results",line):
      f_flag=2 
      detectedNew.write(line) 
      break
    if f_flag==1:
      detectedNew.write(line) 
os.remove("out")
os.chdir(oldpwd)

detectedNew.close()
detectedF=etree.parse("detectedN")
vuls=detectedF.xpath("/results/VulScanResult")
for vul in vuls:
   if vul.xpath("Detected")[0].text=="true": 
      detectedV.append(vul.xpath("Vul_ID")[0].text) 



import tempfile
temp=etree.parse(oldpwd+"/temp.xml")
vuls2=temp.xpath("/GetVulnerabilitiesOfTypeResult/vulnerabilities/vulnerability")
for vul2 in vuls2:
   v2=vul2.xpath("@Vul_ID")[0]
   if v2 in detectedV:
       print vul2.xpath("Patches/Patch/Cmds/Cmd/Args/Arg/@V")[0].replace("&#xA;","\n").replace("&gt;&amp;","&>").replace("&quot;","\"")
       newfile=tempfile.NamedTemporaryFile(delete=False)
       newfile.write(vul2.xpath("Patches/Patch/Cmds/Cmd/Args/Arg/@V")[0].replace("&#xA;","\n").replace("&gt;&amp;","&>").replace("&quot;","\""))
       newfile.close()
       call(["bash",newfile.name])

