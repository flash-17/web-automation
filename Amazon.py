# Automation of Amazon.in
# First command line argument is the search query on amazon
from selenium import webdriver
import time

def main():
	driver = webdriver.Chrome()
	driver.get('http://www.amazon.in')
	search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
	search.send_keys('hp spectre')
	search.submit()

	driver.execute_script("window.scrollTo(0, 200);")
	laptop = driver.find_element_by_xpath('//*[@id="result_1"]/div/div/div/div[2]/div[1]/div[1]/a/h2')
	laptop.click()
	time.sleep(10)

if __name__ == '__main__':
	main()