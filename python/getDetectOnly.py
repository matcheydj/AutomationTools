from lxml import etree
import os,sys,glob,re
import shutil

root=etree.Element('Root')
doc=etree.ElementTree(root)
for f in glob.glob('E:\\mac\\V_[Va-zA-Z0-9_-]*.xml'):
 f0=etree.parse(f)
 state=f0.xpath("/Vulnerability/Status")[0].text
 if state=="Deleted": 
    continue
#  exist=f0.findall("//URL")
#  if re.search("GoogleChrome",f):
#    continue
#  if state=="Deleted": 
#    continue
#  if len(exist)==0:
#    continue
#    
#  try:
#    uniquename=f0.xpath("/Vulnerability/Patches/Patch")[0].attrib['UniqueFilename']
#    try:
#      download=f0.xpath("/Vulnerability/Patches/Patch")[0].attrib['Download']
#    except KeyError:
#      continue
#    if re.match("^\*",uniquename):
#      continue
##    url=f0.xpath("/Vulnerability/Patches/Patch")[0].("URL")
#    url=f0.xpath("/Vulnerability/Patches/Patch")[0].xpath("URL")
#    if len(url)!=0:
#      if uniquename!="" and download=="DManual" and re.match("^http",str(url[0].text)):
#        shutil.copy2(f,"E:\\tmp\\") 
#  except KeyError:
#      shutil.copy2(f,"E:\\tmp\\") 
 type=f0.xpath("//Vulnerability/Patches/Patch")
 type_len=len(type)
 for i in range(type_len):
  uniquename=f0.xpath("/Vulnerability/Patches/Patch")[i].attrib['UniqueFilename']
  if uniquename=="":
    print  f.split("\\")[2]+" : DETECT_ONLY : Remediation of this patch is currently not supported"
    
    name=etree.SubElement(root,'Name')
    type=etree.SubElement(root,'Type')
    reason=etree.SubElement(root,'Reason')
    name.text=f
    type.text='DETECT_ONLY'
    reason.text='Remediation of this patch is currently not supported'
    continue
  if re.match("^\*",uniquename):
    continue
  try:
    download=f0.xpath("/Vulnerability/Patches/Patch")[i].attrib['Download']
    if download=="DManual":
      if re.search("Firefox|SeaMonkey|Thunderbird|ADIUM|SKYPE|MS|Shockwave|AIM|Lync|AdobeAIR|AdobeAir|JavaFor|Safari|JavaUpdate|APPLE-SA|APPLE-SP|OPERA|ParallelsDesktop|APPLE-Messenger|REALPLAYER|Illustrator|PhotoShop|VMware-Fusion|GoogleChrome|iTunes711|JAVA-For10.5Update3|YahooWidgetUpdate_452|Safari7.0.5Mavericks|SymantecEncryptionDesktop10.3",f):
        print  f.split("\\")[2]+" : MANUAL : Vendor\'s URL becomes invalid "
        name=etree.SubElement(root,'Name')
        type=etree.SubElement(root,'Type')
        reason=etree.SubElement(root,'Reason')
        name.text=f
        type.text='MANUAL'
        reason.text='Vendor\'s URL becomes invalid'
      if re.search("JAVA[78]+U",f):
        print  f.split("\\")[2]+" : MANUAL : Requires License/Eula agreement to download/install the patch "
        name=etree.SubElement(root,'Name')
        type=etree.SubElement(root,'Type')
        reason=etree.SubElement(root,'Reason')
        name.text=f
        type.text='MANUAL'
        reason.text='Requires License/Eula agreement to download/install the patch'
      if re.search("FlashPlayer",f):
        print  f.split("\\")[2]+" : DETECT_ONLY : Remediation of this patch is currently not supported "
        name=etree.SubElement(root,'Name')
        type=etree.SubElement(root,'Type')
        reason=etree.SubElement(root,'Reason')
        name.text=f
        type.text='DETECT_ONLY'
        reason.text='Remediation of this patch is currently not supported'
      if re.search("OSXServer|Pages|Xcode|Motion|Numbers|Mainstage|MainStage|iMovie|Keynote|iPhoto|LogicPro|iBooksAuthor|GarageBand|Compressor|Configurator|FinalCutPro|Aperture|RemoteDesktopAdmin|RemoteDesktop",f):
        print  f.split("\\")[2]+" : MANUAL : Requires login to download the patch"
        name=etree.SubElement(root,'Name')
        type=etree.SubElement(root,'Type')
        reason=etree.SubElement(root,'Reason')
        name.text=f
        type.text='MANUAL'
        reason.text='Requires login to download the patch'
#      else:
#	 print  f.split("\\")[2]+" : MANUAL : URL becomes invalid and the patch could not be found "
#         name=etree.SubElement(root,'Name')
#         type=etree.SubElement(root,'Type')
#         reason=etree.SubElement(root,'Reason')
#         name.text=f
#         type.text='DETECT_ONLY'
#         reason.text='Agent could not deal with the installation of the patch'

    
  except  KeyError:
    pass

f=open('NoPatch.txt','w')
doc.write(f,pretty_print=True)
