import os,sys,re
from lxml import etree
import subprocess
import urllib2
import bs4




#def CreateContent(f,p):
#  f0=etree.parse(f)
#  t=f0.xpath("/Vulnerability")[0].attrib['Vul_ID']
#  
#  des=re.sub(t,'MACSWP_'+t,f)
#  f0.xpath("/Vulnerability")[0].attrib['Vul_ID']='MACSWP_'+t
#
#  t2=f0.xpath("//Products/ID")
#  for t3 in t2:
#    t3.text=''
#  t2[0].text=p
#  f0.write(des)
#
#def Vname(f):
#  f2=etree.parse(f)
#  t=f2.xpath("/Vulnerability/Patches/Patch[1]/Name")[0].text
#  if re.search("esr",f):
#    return 'Firefoxesr'
#  else:
#    return t.split()[0]
#
#VP={'Thunderbird':'MACThunderbird17-SLeoLater-Swp','Google':'MAC_GoogleChrome-SLeLater-Swp','Firefoxesr':'MAC_Firefox2410esr_INTEL_Mricks_swp','Firefox':'MacFirefox17-SLeLater-Swp','SeaMonkey':'MACSeaMonkey-SnowLeLater-Swp'}
#
#
#for f in os.listdir('F:/committool/tmp/'):
#  if re.match('[0-9a-zA-Z_.-]*.xml',f):
#   
#    f3='F:\\committool\\tmp\\'+f
#    CreateContent(f3,VP[Vname(f3)])
#

def extract(url,t):
  page=urllib2.urlopen(url)
  soup=bs4.BeautifulSoup(page.read().decode('utf-8'))
  metas=soup.find('meta',{'name':'Description'})
  title=soup.find('meta',{'name':'og:title'})
  if(t=="Title"):
    return title['content']
  if(t=="Description"):
    return metas['content']
#            print str(i['name']).decode('utf-8')
urls={'SVE':'http://download.microsoft.com/download/E/0/A/E0AB3D41-DF3C-4F9E-998D-07F464476CF2/Office2011-1443Update_SV-SE.dmg','JPN':'http://download.microsoft.com/download/8/D/5/8D5A541F-0B69-48C3-9BAD-D6D7773A8FDE/Office2011-1443Update_JA-JP.dmg','ITA':'http://download.microsoft.com/download/1/0/8/10818C33-F397-4FD9-AE88-7EF205DD6404/Office2011-1443Update_IT-IT.dmg','NLD':'http://download.microsoft.com/download/1/9/3/193CD2F9-0EDF-417D-9136-07277FF87901/Office2011-1443Update_NL-NL.dmg','DAN':'http://download.microsoft.com/download/8/E/2/8E21606D-7EF0-4958-B257-768E600FD55F/Office2011-1443Update_DA-DK.dmg','NOR':'http://download.microsoft.com/download/6/5/5/655D83F4-20D2-4423-AD2C-DA6F19787B88/Office2011-1443Update_NB-NO.dmg','PLK':'http://download.microsoft.com/download/7/A/6/7A6629FC-8F8D-46D9-B454-61467745755F/Office2011-1443Update_PL-PL.dmg','ESN':'http://download.microsoft.com/download/2/3/2/2325B9F9-A03D-4EDC-98C5-4DA8D49EE99A/Office2011-1443Update_ES-ES.dmg','RUS':'http://download.microsoft.com/download/B/1/E/B1EA023E-8263-4E89-BB79-A7796B7D4808/Office2011-1443Update_RU-RU.dmg','DEU':'http://download.microsoft.com/download/E/3/A/E3AACB80-F808-4C42-8A32-4D2DF71C0F4E/Office2011-1443Update_DE-DE.dmg','FRA':'http://download.microsoft.com/download/D/B/5/DB50F499-9E42-4341-9C07-9D0E531F1623/Office2011-1443Update_FR-FR.dmg','FIN':'http://download.microsoft.com/download/7/A/2/7A293081-F0AD-459A-B4F5-2062E5BE1588/Office2011-1443Update_FI-FI.dmg','CHT':'http://download.microsoft.com/download/D/C/E/DCE18400-1B53-4E85-B84F-CEAC76B86481/Office2011-1443Update_ZH-TW.dmg','CHS':'http://download.microsoft.com/download/6/5/5/655766C0-DCA5-4473-AD3C-BE30B0869B91/Office2011-1443Update_ZH-CN.dmg'}
langs={"CHS":"ZH-CN","CHT":"ZH-TW","JPN":"JA-JP","DAN":"DA-DK","FIN":"FI-FI","SVE":"SV-SE","NOR":"NB-NO","ESN":"ES-ES","FRA":"FR-FR","ITA":"IT-IT","PLK":"PL-PL","RUS":"RU-RU","NLD":"NL-NL","DEU":"DE-DE"}
f=etree.parse("V_ENU_OFFICE-2011-1443.xml")
for k in langs:
  print k
  t=f.xpath("/Vulnerability")[0].attrib['Lang']
  f.xpath("/Vulnerability")[0].attrib['Lang']=k
  f.xpath("/Vulnerability/Patches/Patch")[0].attrib['UniqueFilename']="Office2011-1443Update_"+langs[k]+".dmg"
  c=os.stat("Office2011-1443Update_"+langs[k]+".dmg").st_size
  f.xpath("/Vulnerability/Patches/Patch")[0].attrib['Size']=str(c)
  hash=subprocess.check_output(['..\hashTool\get_hash.exe','/MD5','Office2011-1443Update_'+langs[k]+'.dmg'])
  ha=hash.rstrip()
  f.xpath("/Vulnerability/Patches/Patch")[0].attrib['Hash']=ha
  f.xpath("/Vulnerability/Patches/Patch/Name")[0].text="Office2011-1443Update_"+langs[k]+".dmg"
  f.xpath("/Vulnerability/Title")[0].text=extract("http://www.microsoft.com/"+langs[k]+"/download/details.aspx?id=43378","Title")
  f.xpath("/Vulnerability/Description")[0].text=extract("http://www.microsoft.com/"+langs[k]+"/download/details.aspx?id=43378","Description")
  f.xpath("/Vulnerability/Patches/Patch/URL")[0].text=urls[k]
  f.write("V_"+k+"_OFFICE-2011-1443.xml")

#  g=etree.parse("V_"+k+"_OFFICE-2011-1441.xml")
#  node=g.find("//Patch")
#  re=g.xpath("/Vulnerability")[0].attrib['Revision']
#  g.xpath("/Vulnerability")[0].attrib['Revision']=str(int(re)+1)
#  node_parent=node.getparent()
#  node.insert(node_parent.index(node)+1,etree.XML(' <SupercededBy Vul_ID="OFFICE-2011-1443" />'))
#  g.write("V_"+k+"_OFFICE-2011-1441.xml")
