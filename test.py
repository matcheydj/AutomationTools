import os,sys,re,time,json
from pymongo import Connection

client=Connection()
mydb=client["test"]
#for i in range(20):
#  mydb.collection1.insert({"num":i})
#for n in mydb.collection1.find():
#  print n
mydb.collection1.remove(None,safe=True)
doc={}
with open("Packages") as f:
  for line in f:
      if(re.match("^$",line)):
        mydb.collection1.insert(dict(doc))
        doc.clear()
        continue
      groups=re.split(": ",line) 
      doc[groups[0]]=groups[1][:-1]
      
