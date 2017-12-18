import os, sys, re
from lxml import etree

class toNew():

  def log(self, g, which):
    if which == 1:
      with open("beforechange", "ab") as l:
        l.write(g + "\n\n\n")
    if which == 2:
      with open("afterchange", "ab") as m:
        m.write(g + "\n\n\n")
  def CreateContent(self, f):
    parser = etree.XMLParser(resolve_entities=False)
    f0 = etree.parse(f, parser=parser)
    encoding = f0.docinfo.encoding
    ret = None
    v = f0.xpath("/Vulnerability/Vendor")[0].text
    if (re.search("LANDesk", str(v)) != None):
      f0.xpath("/Vulnerability/Vendor")[0].text = "LANDESK"
      self.log(f + "\nVendor:" + str(v), 1)
      self.log(f + "\nVendor:LANDESK", 2)
      ret = 2
    t = f0.xpath("/Vulnerability/Title")[0].text
    try:
      if (re.search("LANDesk", t) != None):
          if (re.search("LANDesk", t) != None):
            self.log("Title:" + t, 1)
            f0.xpath("/Vulnerability/Title")[0].text = t.replace("LANDesk", "LANDESK")
            self.log("Title:" + t.replace("LANDesk", "LANDESK"), 2)
	    ret = 2
    except TypeError:
#      pass
      print(f)
    u = f0.xpath("/Vulnerability/Description")[0].text
    try:
      if (re.search("LANDesk", u) != None):
        self.log("Description:" + u.encode("utf-8"), 1)
        f0.xpath("/Vulnerability/Description")[0].text = u.replace("LANDesk", "LANDESK")
        self.log("Description:" + u.replace("LANDesk", "LANDESK"), 2)
        ret = 2 
    except :
#      pass
       print(f)
    
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
for i in os.listdir('F:/committool/tmp/'):
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
      with open("F:\\committool\\tmp\\new\\" + i, "w+") as f4:
        f4.write(r'<?xml version="1.0"?>' + "\n" + fc)
