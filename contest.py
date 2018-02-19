from selenium import webdriver
import time

def main():
	driver = webdriver.Chrome()
	driver.get('http://cloudkentest.herokuapp.com')
	username = driver.find_element_by_xpath('//*[@id="cloud"]')
	username.send_keys('admin')
	password = driver.find_element_by_xpath('//*[@id="ken"]')
	password.send_keys('password')
	time.sleep(4)
	password.submit()
	time.sleep(10)

if __name__ == '__main__':
	main()
