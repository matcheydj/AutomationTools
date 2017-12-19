import os, sys, re
from lxml import etree

class toNew():

  def CreateContent(self, f):
    print(f)
    parser = etree.XMLParser(resolve_entities=False)
    f0 = etree.parse(f, parser=parser)
    encoding = f0.docinfo.encoding
    ret = None
    v = f0.xpath("/Vulnerability")[0].attrib["CVE_ID"].text
    if (re.search(" ", str(v)) != None):
      cve=f0.xpath("/Vulnerability")[0].attrib["CVE_ID"].text 
      f0.xpath("/Vulnerability")[0].attrib["CVE_ID"].text =re.sub(" ","",cve)
      ret = 2
#    u = f0.xpath("/Vulnerability/Description")[0].text
#    if (re.search("LANDesk", u) != None):
#      self.log("Description:" + u.encode('ascii','xmlcharrefreplace'), 1)
#      f0.xpath("/Vulnerability/Description")[0].text = u.replace("LANDesk", "LANDESK")
#      self.log("Description:" + u.encode('ascii','xmlcharrefreplace').replace("LANDesk", "LANDESK"), 2)
#      ret = 2 
#      pass
    
#    self.log("------------")
    if (ret == None):
      return None 
    else:
      revision = f0.xpath("/Vulnerability")[0].attrib["Revision"]
      f0.xpath("/Vulnerability")[0].attrib["Revision"] = str(int(revision) + 1)
#    print  etree.tostring(f0)
#    f0.write(f,xml_declaration=True)
      return f0 


o = toNew()
for i in os.listdir('F:\\committool\\PatchManagerContent\\Vulnerabilities\\mac'):
  if re.match('V[0-9a-zA-Z_. -]*.xml', i):
   
    f3 = 'F:\\committool\\tmp\\' + i
#    print(f3)
    obj = o.CreateContent(f3)
    if (obj == None):
      continue
    else:
# for i in os.listdir('F:/committool/tmp/'):
#  if re.match('V[0-9a-zA-Z_. -]*.xml',i):
#   
#    f3='F:\\committool\\tmp\\'+i
#    print(f3)
#    with open(f3,"a+") as f2:
#      fc=f2.read()
     fc = re.sub('\<\?xml version=\'1.0\' encoding=\'UTF-8\'\?\>', '<?xml version="1.0"?>', etree.tostring(obj))
#      fc=re.sub('&#10;','&#xA;',fc)
     fc = re.sub('([A-Za-z"]+)/>', '\\1 />', fc)
     with open("F:\\committool\\tmp\\" + i, "w+") as f4:
        f4.write(r'<?xml version="1.0"?>' + "\n" + fc)
