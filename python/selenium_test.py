from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
first="http://www.microsoft.com/"
second="/download/details.aspx?id=17198"
xs=["de-DE","fi-FI","fr-FR"]

for x in range(len(xs)):
	ur=first+xs[x]+second
	driver.get(ur)
#       a=driver.find_element_by_xpath("//*[@id=\"ad36995f-7d06-75a1-2c27-34fdf96cc5d9\"]/div/div/div[2]/div[3]/div/div/div/a")
        b="//*[@id=\"ad36995f-7d06-75a1-2c27-34fdf96cc5d9\"]/div/div/div[2]/div[3]/div/div/div/a"
	a= WebDriverWait(driver,10).until(
			EC.visibility_of_element_located((By.XPATH,b))
	)
        a.click()
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

