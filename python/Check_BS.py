from bs4 import BeautifulSoup
import urllib,shutil,os

url=["https://itunes.apple.com/cn/app/os-x-server/id883878097?l=en&mt=12","https://itunes.apple.com/cn/app/imovie/id408981434?l=en&mt=12","https://itunes.apple.com/cn/app/garageband/id682658836?l=en&mt=12","https://itunes.apple.com/cn/app/pages/id409201541?l=en&mt=12","https://itunes.apple.com/cn/app/numbers/id409203825?l=en&mt=12","https://itunes.apple.com/cn/app/keynote/id409183694?l=en&mt=12","https://itunes.apple.com/cn/app/final-cut-pro/id424389933?l=en&mt=12","https://itunes.apple.com/cn/app/motion/id434290957?l=en&mt=12","https://itunes.apple.com/cn/app/compressor/id424390742?l=en&mt=12","https://itunes.apple.com/cn/app/logic-pro-x/id634148309?l=en&mt=12","https://itunes.apple.com/cn/app/mainstage-3/id634159523?l=en&mt=12","https://itunes.apple.com/cn/app/ibooks-author/id490152466?l=en&mt=12","https://itunes.apple.com/cn/app/xcode/id497799835?l=en&mt=12","https://itunes.apple.com/cn/app/apple-remote-desktop/id409907375?l=en&mt=12","https://itunes.apple.com/cn/app/apple-configurator/id434433123?l=en&mt=12","https://itunes.apple.com/cn/app/facetime/id414307850?l=en&mt=12"]

app=open("apps",'r')
appNew=open("appsNew",'w')
#for a in url:
for a in app:
  response=urllib.urlopen(a.split( )[0])
  soup=BeautifulSoup(response)
  ver=soup.select('span[itemprop="softwareVersion"]')[0].text
  appNew.write(a.split()[0]+"   "+ver+"\n")
  if (a.split( )[1] != ver):
    print soup.title.text+"    "+ver
  print soup.select('span[itemprop="softwareVersion"]')[0].text
app.close()
appNew.close()
os.remove("apps")
shutil.copy2("appsNew","apps")
os.remove("appsNew")
