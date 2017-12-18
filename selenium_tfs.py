from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

first="http://slc-tfs3.ld.landesk.com:8080/tfs/LD/SSM"
fp = webdriver.FirefoxProfile()

fp.set_preference("network.automatic-ntlm-auth.trusted-uris","http://slc-tfs3.ld.landesk.com:8080/tfs/LD/SSM")

driver = webdriver.Firefox(firefox_profile=fp)
driver.get(first)
a=driver.find_element_by_id("searchbox")
a.send_keys("322773")
a.send_keys(Keys.RETURN)
driver.execute_script("document.evaluate('/html/body/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[1]/input' ,document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null ).singleNodeValue.setAttribute('title','test content update for mac')")
#driver.get("http://slc-tfs3.ld.landesk.com:8080/tfs/LD/SSM/_workItems/index#id=322345&triage=true&_a=edit")
#b=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[1]/ul/li[6]/span")
#a=driver.find_element_by_id("searchbox")
#        b="//*[@id=\"ad36995f-7d06-75a1-2c27-34fdf96cc5d9\"]/div/div/div[2]/div[3]/div/div/div/a"
#b= WebDriverWait(driver,10).until(
#		EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[1]/ul/li[6]/span"))
#	)
#b.click()
##c=driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/button[1]/span")
#c.click()
#t=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[1]/input")
#d=driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/button[1]");
#d.click()
#driver.execute_script("document.evaluate('/html/body/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[1]/input' ,document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null ).singleNodeValue.setAttribute('title','test content update for mac')")
#t.gettitle.send_keys("test content update for mac")
#a.send_keys("322345")
#a.send_keys(Keys.RETURN)
#for handle in driver.window_handles:
#	print handle
#	print "\n"
#clone=driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[3]/div[3]/div[2]/div/div[2]/div[1]/ul/li[6]/span")
#clone.click()
#select = Select(driver.find_element_by_name('newlocale'))
#for x in range(1,6):
#	select.select_by_index(x)
#	driver.back()
#        select = Select(driver.find_element_by_name('newlocale'))
#assert "Python" in driver.title
#elem = driver.find_element_by_partial_link_text("Update.for.Lync.for.Mac")
#elem.click()
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#driver.save_screenshot('screenshot.jpg')
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()//*[@id="ad36995f-7d06-75a1-2c27-34fdf96cc5d9"]/div/div/div[2]/div[3]/div/div/div/a

