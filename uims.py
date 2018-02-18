from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
	driver = webdriver.Chrome()
	driver.get("https://uims.cuchd.in")

	un = driver.find_element_by_name("txtUserId")
	un.clear()
	un.send_keys('16BCS7017')
	un.send_keys(Keys.RETURN)
	time.sleep(5)

	pw = driver.find_element_by_name('txtLoginPassword')
	pw.clear()
	pw.send_keys('AmaZ^1010')
	pw.send_keys(Keys.RETURN)

	#Logged in successfully
	sidebar = driver.find_element_by_xpath('//*[@id="slide-toggle1"]/a')
	sidebar.click()
	time.sleep(5)

	r0 = driver.find_element_by_xpath('//*[@id="menu-content"]/li[4]/a')
	r0.click()
	time.sleep(10)

	# rl = driver.find_element_by_xpath('//*[@id="menu-content"]/li[11]/a')
	# rl.click()
	# time.sleep(10)



if __name__ == '__main__':
	main()