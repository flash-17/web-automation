from selenium import webdriver
import time

def login():
	driver = webdriver.Chrome()
	driver.get('http://172.16.2.1:1000/login?')
	uid = driver.find_element_by_xpath('//*[@id="ft_un"]')
	uid.send_keys('16BCS7017')
	pw = driver.find_element_by_xpath('//*[@id="ft_pd"]')
	pw.send_keys('AmaZ^1010')
	pw.submit()

def logout():
	driver = webdriver.Chrome()
	driver.get('http://172.16.2.1:1000/logout?')
	time.sleep(3)

if __name__ == '__main__':
	login()