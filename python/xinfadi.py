 # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os,sys,glob,re
import shutil
import urllib
import urllib.request
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd


trace=None
f=open("t.csv",'w',encoding="utf-8")
f.write("Price,Time\n")
for i in range(1,15):
#     local,headers=urllib.request.urlretrieve('http://www.xinfadi.com.cn/marketanalysis/0/list/'+str(i)+'.shtml?prodname=%E5%AF%8C%E5%A3%AB%EF%BC%88%E7%BA%B8%E8%A2%8B%CE%A685%E4%BB%A5%E4%B8%8A%EF%BC%89&begintime=1970-01-01&endtime=2017-01-11')
     local,headers=urllib.request.urlretrieve('http://www.xinfadi.com.cn/marketanalysis/0/list/'+str(i)+'.shtml?prodname=%E5%AF%8C%E5%A3%AB%EF%BC%88%E7%BA%B8%E8%A2%8B%CE%A685%E4%BB%A5%E4%B8%8A%EF%BC%89&begintime=1970-01-01&endtime=2017-01-11')

     soup=BeautifulSoup(open(local,'rt',encoding="utf-8"),"html.parser")
     table=soup.find("table","hq_table")
     
     trs=table.find_all("tr","tr_color")
     for i in trs:
          
          tds=i.find_all("td")
##          trace = go.Scatter(
##             x = tds[2].string,
##             y = tds[6].string
##          )
          f.write(tds[2].string+","+tds[6].string+"\n")
          print("%s          %s" % (tds[2].string,tds[6].string),end="")
##          for t in tds:
##               if t.string is not None:
##                 print("%s          " % (t.string),end="")
          print()


##trace = go.Scatter(
##    x = random_x,
##    y = random_y
##)
##

f.close()

##py.iplot([trace], filename='basic-line')


df = pd.read_csv('t.csv')
df.head()

trace = go.Scatter(
                    x=df['Time'], y=df['Price'], # Data
                    mode='lines' # Additional options
                   )

py.plot([trace], filename='富士（膜袋）_2016')
