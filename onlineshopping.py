from selenium import webdriver
import time

search = 'earphones'

def amazon():
	driver = webdriver.Chrome()
	driver.get('https://www.amazon.in/')
	driver.set_window_rect(0, 0)
	driver.set_window_size(800, 2114)
	searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
	searchbar.send_keys(search)
	searchbar.submit()
	driver.execute_script("window.scrollTo(50, 170)")
	


def flipkart():
	driver = webdriver.Chrome()
	driver.get('https://www.flipkart.com/')
	driver.set_window_rect(800, 0)
	driver.set_window_size(800, 2114)
	time.sleep(5)
	ad = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
	ad.click()
	searchbar = driver.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div/div/div/div[1]/form/div/div[1]/div/input')
	searchbar.send_keys(search)
	searchbar.submit()
	driver.execute_script("window.scrollTo(200, 50)")
	time.sleep(20)


if __name__ == '__main__':
	amazon()
	flipkart()