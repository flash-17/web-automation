from selenium import webdriver
import time

def main():
	driver = webdriver.Chrome()
	driver.get('https://www.studytonight.com/dbms/overview-of-dbms.php')
	driver.execute_script("window.scrollTo(0, 500)")
	time.sleep(5)
	driver.execute_script("window.scrollTo(500, 1000)")
	time.sleep(5)
	driver.execute_script("window.scrollTo(0, 1500)")
	time.sleep(5)


if __name__ == '__main__':
	main()