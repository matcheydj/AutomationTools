from lxml import etree
import os,sys,glob,re,codecs
from copy import deepcopy
from subprocess import call
import argparse
from shutil import copy
import logging
from io import BytesIO
import time

__author__ = "David wang"
__version__ = "2.0"
__maintainer__ = "David wang"
__email__ = "zhaodong.wang@ivanti.com"

#Initialize the logger.
logger=logging.getLogger()
filehandler=logging.FileHandler("log")
streamhandler=logging.StreamHandler()
formatter=logging.Formatter('%(asctime)s %(name)-12s   %(message)s')
filehandler.setFormatter(formatter)
streamhandler.setFormatter(formatter)
logger.addHandler(filehandler)
logger.addHandler(streamhandler)
logger.setLevel(logging.DEBUG)


oldpwd=os.getcwd()
#Analyze the command line arguments, and check the vulnerabilities and products files.
parser=argparse.ArgumentParser(description='Handle command line arguments')
parser.add_argument('--contents_dir',help="this is the directory of contents.")
args=parser.parse_args()
contents_dir=args.contents_dir
check=True
if contents_dir is not  None:
   for v in glob.glob(contents_dir+'/V[a-zA-Z0-9_-]*.xml'):
        fxml=etree.parse(v)
        pids=fxml.xpath("//Products/ID")
        for i in pids:
           if os.path.isfile(contents_dir+"/P_"+i.text+".xml"):
             pass
           else:
             check=False
             logger.debug(("P_"+i.text+".xml is not found!"))
else:
   parser.error("Specify the contents_dir")
   check=False
if  not check:
   sys.exit()

			   

#Produce the final vuldefs file using the template vul.xml 
#vul=b'''<GetVulnerabilitiesOfTypeResult><Merge>false</Merge><vulnerabilities><vulnerability Lang="INTL" Vul_ID="RHSA-2015-2155" CVE_ID="CVE-2014-0207,CVE-2014-0237,CVE-2014-0238,CVE-2014-3478,CVE-2014-3479,CVE-2014-3480,CVE-2014-3487,CVE-2014-3538,CVE-2014-3587,CVE-2014-3710,CVE-2014-8116,CVE-2014-8117,CVE-2014-9652,CVE-2014-9653" Date="1477279601" T="0"><Status>Enabled</Status><Title>Moderate: file security and bug fix update</Title><Patches><Patch Download="DAuto" Silent="CRSUnknown" Reboot="RNo" UniqueFilename="*file-5.11-31.el7.x86_64.rpm" Hash="" Size="0"><Name>file-5.11-31.el7.x86_64.rpm</Name><Advanced><DetectScript /><DetectScriptDescription /></Advanced><Comments /><State>Enabled</State><AdditionalFiles /><Processes /><RunAsUser>false</RunAsUser><PreInstall /><DisableWow64Redirect>false</DisableWow64Redirect><UACElevation>false</UACElevation><AdditionalConfig /><Files><File><Path>file::x86_64</Path><FileDate>0001-01-01T00:00:00-08:00</FileDate><FileSize>0</FileSize><Checksum>cb9e13f23fcdebfd4772448c591bb379</Checksum><Version>5.11-31.el7</Version><CommandID>e</CommandID><Flags>P</Flags></File></Files><RegKeys /><Products><ID></ID></Products><Platforms><ID>rhel7_x86_64</ID></Platforms><UninstallInfo><canBeUninstalled>false</canBeUninstalled><requiresOriginalPatch>false</requiresOriginalPatch><Files /><RegKeys /><Cmds /><RunAsUser>false</RunAsUser><PreInstall /><DisableWow64Redirect>false</DisableWow64Redirect><UACElevation>false</UACElevation><AdditionalConfig /></UninstallInfo><CustVars /><Cmds><Cmd Type="shellscript"> <Args> <Arg N="scriptcode" V="" /> </Args> </Cmd></Cmds></Patch></Patches><DependsOn /></vulnerability></vulnerabilities><products><prod Prod_ID="33752" Revision="1" Date="1477279616"><Name>file 5.x Redhat</Name><Vendor>Redhat</Vendor><Version /><Custom>false</Custom><DetectedByFiles /><DetectedByRegs /><Advanced><DetectScript /><DetectScriptDescription /></Advanced><DetectedByRPMs><RPM><filename>file</filename><minVersion>5.0</minVersion><maxVersion>5.999</maxVersion></RPM></DetectedByRPMs><DetectedByBundles /></prod></products></GetVulnerabilitiesOfTypeResult>'''
vul=b'''<GetVulnerabilitiesOfTypeResult><Merge>false</Merge><vulnerabilities><vulnerability Lang="INTL" Vul_ID="" CVE_ID="" Date="1477279601" T="0"><Status>Enabled</Status><Title></Title><Patches><Patch Download="DAuto" Silent="CRSUnknown" Reboot="RNo" UniqueFilename="" Hash="" Size="0"><Name></Name><Advanced><DetectScript /><DetectScriptDescription /></Advanced><Comments /><State>Enabled</State><AdditionalFiles /><Processes /><RunAsUser>false</RunAsUser><PreInstall /><DisableWow64Redirect>false</DisableWow64Redirect><UACElevation>false</UACElevation><AdditionalConfig /><Files><File><Path>file::x86_64</Path><FileDate>0001-01-01T00:00:00-08:00</FileDate><FileSize>0</FileSize><Checksum></Checksum><Version></Version><CommandID>e</CommandID><Flags>P</Flags></File></Files><RegKeys /><Products><ID></ID></Products><Platforms><ID></ID></Platforms><UninstallInfo><canBeUninstalled>false</canBeUninstalled><requiresOriginalPatch>false</requiresOriginalPatch><Files /><RegKeys /><Cmds /><RunAsUser>false</RunAsUser><PreInstall /><DisableWow64Redirect>false</DisableWow64Redirect><UACElevation>false</UACElevation><AdditionalConfig /></UninstallInfo><CustVars /><Cmds><Cmd Type="shellscript"> <Args> <Arg N="scriptcode" V="" /> </Args> </Cmd></Cmds></Patch></Patches><DependsOn /></vulnerability></vulnerabilities><products><prod Prod_ID="" Revision="1" Date="1477279616"><Name></Name><Vendor>Redhat</Vendor><Version /><Custom>false</Custom><DetectedByFiles /><DetectedByRegs /><Advanced><DetectScript /><DetectScriptDescription /></Advanced><DetectedByRPMs><RPM><filename>file</filename><minVersion></minVersion><maxVersion></maxVersion></RPM></DetectedByRPMs><DetectedByBundles /></prod></products></GetVulnerabilitiesOfTypeResult>'''
xmlparser=etree.XMLParser(encoding="utf-8")
template=etree.parse(BytesIO(vul),xmlparser)
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
  if len(f0.xpath("@CVE_ID")) != 0:
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
#SLES contents use script for detecting.	  
	  if len(p.xpath("Files/File")) ==0:
             element.xpath("Advanced/DetectScript")[0].text=p.xpath("Advanced/DetectScript")[0].text
#RHEL and CentOS contents use file rules for detecting.
	  if len(p.xpath("Files/File")) !=0:
            element.xpath("Files/File/Path")[0].text=p.xpath("Files/File/Path")[0].text
            if len(p.xpath("Files/File/Checksum")) != 0: 
               element.xpath("Files/File/Checksum")[0].text=p.xpath("Files/File/Checksum")[0].text
            element.xpath("Files/File/Version")[0].text=p.xpath("Files/File/Version")[0].text
          platformEle=element.xpath("Platforms/ID")[0]
          plat_flag=0
          platformIDs=p.xpath("Platforms/ID")
	  for platformID in platformIDs:
            plat=platformEle
	    if plat_flag >0:
               plat=deepcopy(platformEle)
               plat_flag+=1
            plat.text=platformID.text
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
          if p.xpath("@UniqueFilename")[0] != "":
             if len(p.xpath("Cmds/Cmd/Args/Arg/@V")) != 0:
                element.xpath("Cmds/Cmd/Args/Arg")[0].set("V",p.xpath("Cmds/Cmd/Args/Arg/@V")[0].replace("\n","&#xA;").replace("\r","").replace("&>","&gt;&amp;").replace("\"","&quot;"))
          patchEle.getparent().append(element)
          logger.debug(p.xpath("@UniqueFilename")[0]+" is added to temp.xml.") 
          flag+=1

  logger.debug(f0.xpath("@Vul_ID")[0]+" is added to temp.xml.") 


#Add products info to the final vuldefs file.
prodEle=template.xpath("/GetVulnerabilitiesOfTypeResult/products/prod")[0]
prodEleBak=deepcopy(prodEle)
prod_flag=0
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
   logger.debug("Product "+i2.text+" is added to temp.xml.") 
  
template.write(oldpwd+"/temp.xml")
logger.debug('vulnerability file temp.xml is done!')

#Do the detection with the final vuldefs file and save the results to /opt/landesk/bin/out.
from subprocess import call
import time
detectedV=[]
detectedNew=open("detectedVul","w")
os.chdir("/opt/landesk/bin/")
logger.debug("vulscan is running!")
call(["./vulscan","-d",oldpwd+"/temp.xml","-o","out","-V0"])
while not os.path.isfile("out"):
   time.sleep(3) 
logger.debug("The following are the vulscan result:")
emptyout=0
with open("/opt/landesk/bin/out") as detected:
  f_flag=0
  for line in detected:
    if re.search("<results/",line):
      logger.debug("No vulnerabilities are targeted for this platform!")
      emptyout=1
      break
    if re.search("<results",line):
      f_flag=1 
    if re.search("</results",line):
      f_flag=2 
      detectedNew.write(line)
      logger.debug(line)
      break
    if f_flag==1:
      detectedNew.write(line)
      logger.debug(line)
os.remove("out")
logger.debug('/opt/landesk/bin/out is deleted!')
os.chdir(oldpwd)
if emptyout == 1:
   os.remove("temp.xml")
   os.remove("detectedVul")
   sys.exit()
detectedNew.close()

detectedF=etree.parse("detectedVul")
vuls=detectedF.xpath("/results/VulScanResult")
report=etree.parse(BytesIO("<Report></Report>"))
for vul in vuls:
   vulbak=deepcopy(vul)
   report.xpath("/Report")[0].append(vulbak)
   if vul.xpath("Detected")[0].text=="true": 
      detectedV.append(vul.xpath("Patch")[0].text) 


#Repair the detected vulnerabilities.
import tempfile
temp=etree.parse(oldpwd+"/temp.xml")
vuls2=temp.xpath("/GetVulnerabilitiesOfTypeResult/vulnerabilities/vulnerability/Patches/Patch")
repairDict={}
for vul2 in vuls2:
   v2=vul2.xpath("@UniqueFilename")[0]
   if v2 == "":
     continue
   if v2 in detectedV:
       print(vul2.xpath("Cmds/Cmd/Args/Arg/@V")[0].replace("&#xA;","\n").replace("&gt;&amp;","&>").replace("&quot;","\""))
       logging.debug("Prepare to repair "+v2)
       newfile=tempfile.NamedTemporaryFile(delete=False)
       newfile.write(vul2.xpath("Cmds/Cmd/Args/Arg/@V")[0].replace("&#xA;","\n").replace("&gt;&amp;","&>").replace("&quot;","\""))
       newfile.close()
       ret=call(["bash","-x",newfile.name])
       if ret == 0:
         logging.debug(v2+" is repaired successfully!")
         repairDict[v2]="true"
       else:
         logging.debug(v2+" is not repaired !")
         repairDict[v2]="false"
         
#Produce the final repairing report.
reportvs=report.xpath("/Report/VulScanResult")
for reportv in reportvs:
  reportkey=reportv.xpath("Patch")[0].text
  if reportkey in repairDict:
    if repairDict[reportv.xpath("Patch")[0].text] == "true":
       reportv.append(etree.fromstring("<Repaired>true</Repaired>"))    
    else:
       reportv.append(etree.fromstring("<Repaired>false</Repaired>"))    
    
timestr=time.strftime("%y%m%d-%H%M",time.localtime())
report.write("Report"+timestr+".xml")
os.remove("temp.xml")
os.remove("detectedVul")
