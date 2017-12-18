import requests
url ='https://www.magentocommerce.com/products/customer/account/loginPost/referer/aHR0cHM6Ly93d3cubWFnZW50b2NvbW1lcmNlLmNvbS9wcm9kdWN0cy9jdXN0b21lci9hY2NvdW50Lw,,/'
values= {'login[back_url]': 'https://www.magentocommerce.com/products/customer/account/',
	  'form_key': 'zwxaJ9O5XbT7FBol',
          'login[username]': 'wangzhaodong8@126.com',
          'login[password]': '!LANDesk123',
	  'send':''}

cookies = {'frontend':'mh6ebgjipt777aph4pr1vbgkb5'}
po=requests.post(url, data=values,cookies=cookies)
#cookies = {'frontend':'mh6ebgjipt777aph4pr1vbgkb5','optimizelyEndUserId':'oeu1449218896261r0.5158201672192213','totango.heartbeat.last_module':'__system','totango.heartbeat.last_ts':'1449219233898','_ga':'GA1.2.1212115093.1449219011','_gat':'1'}
#cookies = {'frontend':'mh6ebgjipt777aph4pr1vbgkb5','optimizelyEndUserId':'oeu1449218896261r0.5158201672192213','_ga':'GA1.2.1212115093.1449219011','_gat':'1'}
#cookies = {'frontend':'mh6ebgjipt777aph4pr1vbgkb5','optimizelyEndUserId':'oeu1449218896261r0.5158201672192213'}

#print po.content
info=requests.get("https://www.magentocommerce.com/products/downloads/magento/loggedin/",cookies=cookies)
print info.content



#import cookielib
#import urllib
#import urllib2
#import  requests
#
#url ='https://www.magentocommerce.com/products/customer/account/loginPost/referer/aHR0cHM6Ly93d3cubWFnZW50b2NvbW1lcmNlLmNvbS9wcm9kdWN0cy9jdXN0b21lci9hY2NvdW50Lw,,/'
#values= {'login[back_url]': 'https://www.magentocommerce.com/products/customer/account/',
#	  'form_key': 'mhWnup2FIxsJESp0',
#          'login[username]': 'wangzhaodong8@126.com',
#          'login[password]': '!LANDesk123'}
#data = urllib.urlencode(values)
#cookies = cookielib.CookieJar()
#
#opener = urllib2.build_opener(
#    urllib2.HTTPRedirectHandler(),
#    urllib2.HTTPHandler(debuglevel=0),
#    urllib2.HTTPSHandler(debuglevel=0),
#    urllib2.HTTPCookieProcessor(cookies))
#
#response = opener.open(url, data)
#info=requests.get("https://www.magentocommerce.com/products/downloads/magento/loggedin/")
#print info.content

#import cookielib,urllib, urllib2,requests
#
#cj = cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
## default User-Agent ('Python-urllib/2.6') will *not* work
#opener.addheaders = [
#    ('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.11) Gecko/20101012 Firefox/3.6.11'),
#    ]
#
#url ='https://www.magentocommerce.com/products/customer/account/loginPost/referer/aHR0cHM6Ly93d3cubWFnZW50b2NvbW1lcmNlLmNvbS9wcm9kdWN0cy9jdXN0b21lci9hY2NvdW50Lw,,/'
#values= {'login[back_url]': 'https://www.magentocommerce.com/products/customer/account/',
#	  'form_key': 'KKWiBWSW4DuRKiah',
#          'login[username]': 'wangzhaodong8@126.com',
#          'login[password]': '!LANDesk123'}
#data = urllib.urlencode(values)
#
#
#response = opener.open(url, data)
#info=requests.get("https://www.magentocommerce.com/products/downloads/magento/loggedin/")
#print info.content
#
#
#
#HTTP/1.1 302 Moved Temporarily
#Server: nginx
#Date: Fri, 04 Dec 2015 08:54:16 GMT
#Content-Type: text/html; charset=UTF-8
#Transfer-Encoding: chunked
#Connection: keep-alive
#P3P: CP="NOI ADM DEV PSAi COM NAV OUR OTRo STP IND DEM"
#Expires: Thu, 19 Nov 1981 08:52:00 GMT
#Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
#Pragma: no-cache
#Set-Cookie: frontend=mh6ebgjipt777aph4pr1vbgkb5; expires=Sat, 05-Dec-2015 08:54:15 GMT; path=/; domain=www.magentocommerce.com
#Location: https://www.magentocommerce.com/products/customer/account/
#X-Frame-Options: SAMEORIGIN

#POST /products/customer/account/loginPost/referer/aHR0cHM6Ly93d3cubWFnZW50b2NvbW1lcmNlLmNvbS9wcm9kdWN0cy9jdXN0b21lci9hY2NvdW50Lw,,/ HTTP/1.1
#Host: www.magentocommerce.com
#User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#Accept-Language: en-US,en;q=0.5
#Accept-Encoding: gzip, deflate
#Referer: https://www.magentocommerce.com/products/customer/account/login/
#Cookie: frontend=mh6ebgjipt777aph4pr1vbgkb5; frontend=mh6ebgjipt777aph4pr1vbgkb5; optimizelyEndUserId=oeu1449218896261r0.5158201672192213; totango.heartbeat.last_module=__system; totango.heartbeat.last_ts=1449219233898; optimizelySegments=%7B%22239237138%22%3A%22direct%22%2C%22237962548%22%3A%22ff%22%2C%22238367687%22%3A%22false%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.2.1212115093.1449219011; _gat=1; optimizelyPendingLogEvents=%5B%5D
#Connection: keep-alive
