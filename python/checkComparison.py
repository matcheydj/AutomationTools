from difflib import Differ
import re
import glob

def check(file1,file2):
  a=open(file1)
  b=open(file2)
  missing_from_a = [ diff[2:] for diff in Differ().compare(a.readlines(), b.readlines()) if  diff.startswith('+') or diff.startswith('-') ]
#  missing_from_b = [ dif[2:] for dif in Differ().compare(a.readlines(), b.readlines()) if dif.startswith('-') ]
  print missing_from_a
  for i in range(len(missing_from_a)):
    if i%2!=0:
	    continue
    words_a=re.split('[<>]',missing_from_a[i])
    words_b=re.split('[<>]',missing_from_a[i+1])
    for k in range(len(words_a)):
	    if words_a[k] != words_b[k]:
		    print words_a[k]+"   "+words_b[k]+"\n"

#  if not (len(missing_from_b)==2 and re.match(r' *<Vulnerability',missing_from_b[0]) and re.match(r' *<Description',missing_from_b[1])):
#    print "error"
#  a.close()
#  b.close()
#for f in glob.glob('z:\david\\tmp\HPUX\*.xml'):
#	ss=re.split('[:\\\]*',str(f))
#	check(f,'F:\committool\PatchManagerContent\Vulnerabilities\HPUX\\'+ss[-1])
check('V_INTL_Xcode6.0.1_Update.xml','V_INTL_Xcode6.0.1_Update2.xml')
