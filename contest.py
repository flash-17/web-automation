from selenium import webdriver
import time
def main():

	driver = webdriver.Chrome()
	driver.get('https://cloudkentest.herokuapp.com')
	username = driver.find_element_by_id('userid')
	username.send_keys('admin')
	password = driver.find_element_by_id('password')
	password.send_keys('password')
	password.submit()
	time.sleep(10)
	

if __name__ == '__main__':
	main()