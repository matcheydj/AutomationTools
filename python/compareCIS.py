import os,sys,re

wordsdict={}
uniq=[]
with open("CIS2.1.1.txt") as newf:
  for line in newf:
    words=line.split()
    for w in words:
      if w in wordsdict:
       wordsdict[w]+=1
      else:
       wordsdict[w]=1
#    print(min(wordsdict,key=wordsdict.get))
for i in sorted(wordsdict,key=wordsdict.get):
  if wordsdict[i]<4:
      uniq.append(i)

with open("CIS1.0.txt") as f:
  li=f.read().splitlines()

with open("CIS2.1.1.txt") as newf:
  for line in newf:
    words=line.split()
    wordsdict={}
    for w in words:
     num=0
     if w in uniq: 
       for i in li:
         if re.search(w,i):
            num+=1
       wordsdict[w]=num
    if len(wordsdict)==0:
      print(line)
#      print(wordsdict)
