import os,re,glob,subprocess
import shutil


out=subprocess.getoutput('E:/tools/maketoc/MakeTOC.exe z:\mac')

outa=out.split('\n')

for i in outa:
  if re.search("\[[a-zA-Z0-9._-]+\]",i):
    pID=i.split(" ")[3].replace('[','').replace(']','')
    shutil.move("z:\mac\P_"+pID+".xml","F:/mac/")

		

