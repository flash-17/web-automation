#Research.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

topic = 'handshaking'

def window1():
	driver = webdriver.Chrome()
	driver.get('https://www.google.co.in/#q=' + topic)
	time.sleep(5)
	driver.set_window_rect(0, 0)
	driver.set_window_size(800, 550)

def window2():
	driver = webdriver.Chrome()
	driver.get('https://en.wikipedia.org/wiki/' + topic)
	time.sleep(5)
	driver.set_window_rect(800, 0)
	driver.set_window_size(800, 550)

def window3():
	driver = webdriver.Chrome()
	driver.get('http://notes.io')
	driver.set_window_rect(0, 560)
	driver.set_window_size(1600, 300)
	driver.execute_script("window.scrollTo(0, 50)")
	time.sleep(50)


if __name__ == '__main__':
	window1()
	window2()
	window3()