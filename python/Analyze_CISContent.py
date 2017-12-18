import os,re
from lxml import etree





category={"1":"Filesystem and Updates","2":"OS Services","3":"Special Services","4":"Network and Firewalls","5":"Logging and Auditing","6":"System","7":"Accounts and Environment","8":"Warning Banners","9":"Maintenance"}
vulID={"1":"Filesystem","2":"Services","3":"SpecialServices","4":"Network","5":"LogAudit","6":"System","7":"Accounts","8":"Banners","9":"Maintenance"}
f=open("rhel7.txt")
def extract(fh):
        desc=""
        flag=0
	title=""
	level=0
	levels=""
	for l in fh:
	  if re.match("^$",l):
		  continue
	  if (flag == 1):
	          desc+=l	  
	  if (level == 1):
                  levels=l
		  level=0
	  if re.match("^[0-9].[0-9].*Scored", l):
		  title=l 
	  if re.match("Profile Applicability:", l):
                  level=1
		  continue
	  if re.match("^Description:", l):
		  flag=1
	  if re.match("^Rationale:",l):
		  desc=re.sub("Rationale:","",desc)
		  t=re.split(" ",title)
		  name=re.sub("^[0-9\.]* |\([a-zA-Z ]*\)","",title)
		  if (len(re.split("\.",t[0]))==2): 
		    v1,v2=re.split("\.",t[0])
		    v11="-%02d" % int(v1)
		    v2="-%02d" % int(v2)
		    vid="RHEL7-"+vulID[v1]+v11+v2
		    print vid
		  if (len(re.split("\.",t[0]))==3): 
		    v1,v2,v3=re.split("\.",t[0])
		    v11="-%02d" % int(v1)
		    v2="-%02d" % int(v2)
		    v3="-%02d" % int(v3)
		    vid="RHEL7-"+vulID[v1]+v11+v2+v3
		    print vid
		  if (len(re.split("\.",t[0]))==4): 
		    v1,v2,v3,v4=re.split("\.",t[0])
		    v11="-%02d" % int(v1)
		    v2="-%02d" % int(v2)
		    v3="-%02d" % int(v3)
		    v4="-%02d" % int(v4)
		    vid="RHEL7-"+vulID[v1]+v11+v2+v3+v4
		    print vid
		  print category[t[0][0]]

		  group="Internet Security Benchmarks + Red Hat Enterprise Linux 7 Level "+re.search("[0-9]+",levels).group(0)
		  print group
		  desc+="Note: This content will only provide detection of the security threat or vulnerability.  Remediation must be performed manually."
		  print desc
		  CreateContent("F:\\scripts\\python\\contents\\V_INTL_RHEL6-Filesystem-01-01-01.xml",vid,name.rstrip("\n"),group,desc,"V_INTL_"+vid+".xml",category[t[0][0]])
		  

		  flag=0
		  group=desc=v1=v11=v2=v3=v4=vid=t=""
def CreateContent(f,vid,name,group,desc,fname,category):
  f0=etree.parse(f)
  f0.xpath("/Vulnerability")[0].attrib['Vul_ID']=vid
  f0.xpath("/Vulnerability/Groups/Group")[0].text=group
  f0.xpath("/Vulnerability/Description")[0].text=desc
  f0.xpath("/Vulnerability/Title")[0].text=name
  f0.xpath("/Vulnerability/Category")[0].text=category
  f0.xpath("/Vulnerability/Patches/Patch")[0].attrib['UniqueFilename']="*"+name+"(Detect Only)"
  f0.xpath("/Vulnerability/Patches/Patch/Name")[0].text=name+"(Detect Only)"
  

  f0.write(fname)
  with open(fname, "w+") as f4:
    f4.write(r'<?xml version="1.0" encoding="UTF-8"?>' + "\n" + etree.tostring(f0))

extract(f)
