from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def main():
	driver = webdriver.Chrome()
	driver.get("https://uims.cuchd.in")

	un = driver.find_element_by_name("txtUserId")
	un.clear()
	un.send_keys('16BCS7017')
	un_submit = driver.find_element_by_xpath('//*[@id="btnNext"]')
	un_submit.click()
	time.sleep(3)

	pw = driver.find_element_by_name('txtLoginPassword')
	pw.clear()
	pw.send_keys('AmaZ^1010')
	pw_submit = driver.find_element_by_xpath('//*[@id="btnLogin"]')
	pw_submit.click()

	time.sleep(3)

	r0 = driver.find_element_by_xpath('//*[@id="slide-toggle1"]/a')
	r0.click()
	time.sleep(2)
	r1 = driver.get('https://uims.cuchd.in/UIMS/frmStudentCourseWiseAttendanceSummary.aspx')
	time.sleep(20)



if __name__ == '__main__':
	main()
