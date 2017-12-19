import os,sys,re
from lxml import etree


def CreateContent(f,p):
  f0=etree.parse(f)
  t=f0.xpath("/Vulnerability")[0].attrib['Vul_ID']
  
  des=re.sub(t,'MACSWP_'+t,f)
  f0.xpath("/Vulnerability")[0].attrib['Vul_ID']='MACSWP_'+t

  t2=f0.xpath("//Products/ID")
  for t3 in t2:
    t3.text=''
  t2[0].text=p
  f0.write(des)

def Vname(f):
  f2=etree.parse(f)
  t=f2.xpath("/Vulnerability/Patches/Patch[1]/Name")[0].text
  if re.search("esr",f):
    return 'Firefoxesr'
  else:
    return t.split()[0]

VP={'Thunderbird':'MACThunderbird17-SLeoLater-Swp','Google':'MAC_GoogleChrome-SLeLater-Swp','Firefoxesr':'MAC_Firefox2410esr_INTEL_Mricks_swp','Firefox':'MacFirefox17-SLeLater-Swp','SeaMonkey':'MACSeaMonkey-SnowLeLater-Swp','Adobe':'MACSWP_ShockwavePlayerLine_Later2_INTEL'}


for f in os.listdir('F:/committool/tmp/'):
  if re.match('[0-9a-zA-Z_.-]*.xml',f):
    f3='F:\\committool\\tmp\\'+f
    CreateContent(f3,VP[Vname(f3)])
