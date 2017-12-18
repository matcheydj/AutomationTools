import os,re,glob
from lxml import etree
import xlwt


wb=xlwt.Workbook()
apps=wb.add_sheet("Third_Party_App")
os.chdir('z:/mac')
l=[]
for i in glob.glob('V[a-zA-Z0-9._-]*.xml'):
  f=etree.parse(i)
  state=f.xpath("/Vulnerability/Status")[0].text
  lang=f.xpath("/Vulnerability")[0].attrib['Lang']
  vendor=f.xpath("/Vulnerability/Vendor")[0].text
  if vendor == "Apple":
    continue
  if lang == "INTL" or lang == "ENU":
          
    
    if state == "Enabled":
      name=f.xpath("/Vulnerability/Title")[0].text
      fields=name.split(" ")
      if fields[0] == "Skype":
        l.append(fields[0])
        print(fields[0])
        continue

      if re.search("Firefox",name,re.IGNORECASE):
        l.append("Firefox")
        print(fields[0])
        continue

      if re.search("Thunderbird",name,re.IGNORECASE):
        l.append("Thunderbird")
        print(fields[0])
        continue

      if re.search("vlc",name,re.IGNORECASE):
        l.append("vlc")
        print(fields[0])
        continue

      if fields[0] == "Java":
        nameC=" ".join(fields[0:2])
        l.append(nameC)
        print(nameC)
        continue
      for i in range(0,len(fields)):
        if re.search("[0-9]+\.[0-9]*",fields[i]):
                nameA=" ".join(fields[0:i])
                l.append(nameA)
                print(nameA)

j=0
for i in list(set(l)):
  apps.write(j,0,i)
  j+=1

wb.save("third_party_apps")
