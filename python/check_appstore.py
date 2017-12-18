from selenium import webdriver


url=["https://itunes.apple.com/cn/app/os-x-server/id883878097?l=en&mt=12","https://itunes.apple.com/cn/app/imovie/id408981434?l=en&mt=12","https://itunes.apple.com/cn/app/garageband/id682658836?l=en&mt=12","https://itunes.apple.com/cn/app/pages/id409201541?l=en&mt=12","https://itunes.apple.com/cn/app/numbers/id409203825?l=en&mt=12","https://itunes.apple.com/cn/app/keynote/id409183694?l=en&mt=12","https://itunes.apple.com/cn/app/final-cut-pro/id424389933?l=en&mt=12","https://itunes.apple.com/cn/app/motion/id434290957?l=en&mt=12","https://itunes.apple.com/cn/app/compressor/id424390742?l=en&mt=12","https://itunes.apple.com/cn/app/logic-pro-x/id634148309?l=en&mt=12","https://itunes.apple.com/cn/app/mainstage-3/id634159523?l=en&mt=12","https://itunes.apple.com/cn/app/ibooks-author/id490152466?l=en&mt=12","https://itunes.apple.com/cn/app/xcode/id497799835?l=en&mt=12","https://itunes.apple.com/cn/app/apple-remote-desktop/id409907375?l=en&mt=12","https://itunes.apple.com/cn/app/apple-configurator/id434433123?l=en&mt=12","https://itunes.apple.com/cn/app/facetime/id414307850?l=en&mt=12"]


apps=open('apps','r')
driver=webdriver.Firefox()
for a in apps:
#for a in url:
  driver.get(a.split( )[0])
#  driver.get(a)
  name=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[1]/div[1]/h1")
  version=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[3]/div[1]/ul/li[4]/span[2]")
#  print name.text+":"+version.text
  if (a.split( )[1] != version.text):
     print name.text+":"+version.text
#  apps.write(a+"  "+version.text+"\n")
driver.close()

