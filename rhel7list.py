from urllib2 import urlopen 
import  pprint
import json

import urllib2

url="https://access.redhat.com/errata/69/ver=/rhel---7/x86_64/datatable?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength=100&sSearch=&bRegex=false&sSearch_0=&bRegex_0=false&bSearchable_0=true&sSearch_1=&bRegex_1=false&bSearchable_1=true&sSearch_2=&bRegex_2=false&bSearchable_2=true&sSearch_3=&bRegex_3=false&bSearchable_3=true&iSortingCols=1&iSortCol_0=3&sSortDir_0=desc&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=true"

header = {'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Referer': 'https://access.redhat.com/downloads/content/69/ver=/rhel---7/7.0/x86_64/product-errata', 'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko', 'Host': 'access.redhat.com', 'DNT': '1', 'Connection': 'Keep-Alive','Cookie': 's_fid=20E4EB50789E7FCC-07E92B08C10968C4; rh_omni_tc=70160000000H4AjAAK; s_nr=1406173712323; s_vnum=1408765139269%26vn%3D13; s_vi=[CS]v1|29E83FEB851D3D7F-40000134A0004832[CE]; chrome_user_remember=%7B%22login%22%3A%22msahmu%22%2C%22remembered%22%3Atrue%7D; rh_elqCustomerGUID=47ac7935-51bb-40ef-862e-093e23a21c9e; s_cc=true; s_ria=flash%2011%7Csilverlight%202.9; s_dmdbase=rsp%3Dmatch%26cData%3D664254%253ALandesk%253ASoftware%2520%2526%2520Technology%253ASoftware%2520Applications%253AMid-Market%253A%25241B%2520-%2520%25242.5%253AEnterprise%2520Business%253ASoftware%2520%2526%2520Technology%26cDataCustom%3D%253A%253A%253A%253A%253A%253A%253A%26sentAA%3DT; s_sq=redhatglobal%2Credhatcustomerportal%3D%2526pid%253Dcp%252520%25257C%252520u-download%252520%25257C%252520product-list%252520%25257C%252520Red%252520Hat%252520Enterprise%252520Linux%252520Server%2525207%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Faccess.redhat.com%25252Fdownloads%25252Fcontent%25252F69%25252Fver%25253D%25252Frhel---7%25252F7.0%25252Fx86_64%25252Fproduct-errata%2526ot%253DA%2526oi%253D718%26redhatcomglobal%3D%2526pid%253Dhttps%25253A%25252F%25252Fwww.redhat.com%25252Fwapps%25252Fsso%25252Flogin.html%25253Fredirect%25253Dhttp%2525253A%2525252F%2525252Faccess.redhat.com%2525252Fmanagement%2526oid%253DLog%252520In%2526oidt%253D3%2526ot%253DSUBMIT%2526oi%253D47; rh_shared_auth=2ee41d4597cb339ec75a09325eb61852aa2a3f57e4d9fe9b6d3da51548943156fef70fc352ac297a6320a0f3c68a04911ce0f344cc482af8dcb0de26cdd25835; rh_sso=0|SJvdewDfv5tgHPftA7UOHK7wbVmB53csVMD; rh_user=msahmu|Mark|customer|; rh_locale=en_US; chrome_user_info=%7B%22authorized%22%3Atrue%2C%22internal%22%3Afalse%2C%22login%22%3A%22msahmu%22%2C%22user_id%22%3A5112758%2C%22account_id%22%3A5619706%2C%22account_number%22%3A1047346%2C%22email%22%3A%22mark.ahmu@landesk.com%22%2C%22name%22%3A%22Mark%20AhMu%22%2C%22lang%22%3A%22en%22%2C%22lang_err_msg%22%3A%22The%20page%20you%20have%20selected%20is%20not%20yet%20available%20in%20English.%20We%20are%20working%20to%20make%20sure%20all%20content%20is%20available%20in%20English%2C%20but%20in%20order%20to%20display%20the%20page%20we%20have%20switched%20your%20language%20to%20English.%22%2C%22hello%22%3A%22Hello%2C%22%2C%22description_placeholder%22%3A%22Enter%20a%20description%22%7D; s_invisit=true; JSESSIONIDSSO=bCdAVxjQ+uVfF7lF5VW+HvKb; _rhsm-web_session=BAh7CEkiD3Nlc3Npb25faWQGOgZFRkkiJTkxNjVhZTNiOWZmNGQ2MzEyZjE3N2U3OGViODg5NzYwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXRvMGhiWWpJWTlDZTREeWt0MnlheG5UT3hEdlc5aUtHM25BTWppSVVYY1k9BjsARkkiDnJldHVybl90bwY7AEZJIipodHRwczovL2FjY2Vzcy5yZWRoYXQuY29tL21hbmFnZW1lbnQvBjsAVA%3D%3D--ecab37f477bb3c2f393e8125b8e0f7436fd0007f; chrome_session_id=603876|1406855437627; JSESSIONID=hCEwxD2yTtsNughYtZAER7TJ; gwss=rd202o00000000000000000000ffff0a056767o8080; _redhat_downloads_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFRkkiJTMwOWU0NGY5OGRkZmI2YTg1NWY5MjAwNjIwNzViZDRmBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXlXUStWVlZ5MWVoaXlLNHlCVE02YzNWVzlZRWk3ZlBZcTVZcVhzL21YMEU9BjsARg%3D%3D--99e083a5c58816c870d5aa92f9297276b514973f'}

#Debug Log star

httpHandler = urllib2.HTTPHandler(debuglevel=0)

httpsHandler = urllib2.HTTPSHandler(debuglevel=0)

opener = urllib2.build_opener(httpHandler, httpsHandler)

urllib2.install_opener(opener)

#Debug Log end

request = urllib2.Request(url,headers = header)

res = urlopen(request) 

html = res.read()

d=dict(json.loads(html))
for i in d["aaData"]:
  print i[0]
  print i[1]
  print i[2]
  print i[3]
res.close() 


