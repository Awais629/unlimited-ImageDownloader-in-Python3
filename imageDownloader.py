import time
from configure import *
from selenium import webdriver
from selenium.webdriver.common.by import By
if BROWSER.upper() == "CHROME":
	from selenium.webdriver.chrome.options import Options
if BROWSER.upper() == "FIREFOX":
	from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from random import shuffle
import urllib.parse as urlparse
from os.path import join, dirname
import urllib.request


def Launch():
	StartBrowser()

def StartBrowser():
	if PRINT_SETTINGS:
		print("\n\n------SETTINGS------")
		print("BROWSER:"+BROWSER)
		print("HEADLESS:"+str(HEADLESS))
		print("PRINT_ACTIONS:"+str(PRINT_ACTIONS))
		print("PRINT_SETTINGS:"+str(PRINT_SETTINGS))
		print("PARSER:"+PARSER)
		print("VERBOSE:"+str(VERBOSE))
		print("-----------------------------\n\n")


	if BROWSER.upper() == "CHROME":
		if PRINT_ACTIONS:
			print('\n-> Launching Chrome')
		options = Options()
		if HEADLESS:
			print("\t*Chrome will not run correctly in headless mode, starting normal mode.")
		
		browser = webdriver.Chrome(options=options)
	elif BROWSER.upper() == "FIREFOX":
		if PRINT_ACTIONS:
			print('\n-> Launching Firefox')
		options = Options()
		if HEADLESS:
			options.headless = True
		browser = webdriver.Firefox(options=options)
	else:
		print("!!! Browser type not recognized, please check your configure.py - BROWSER="+BROWSER)

	x= 0
	for x in range(5):
		url = "https://opensea.io/assets/ethereum/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/" + str(x)
		print(url)
		browser.get(url)
		time.sleep(2)
		src = browser.find_element(By.XPATH, "//img[contains(@class,'Image--image')]").get_attribute("src")
		print(src)
		loc = "/Users/muhammadawais/Downloads/LinkedIn-Bot-1-master/Screenshots/" + str(x) + ".jpg"
		urllib.request.urlretrieve(src, loc)
		time.sleep(2)

		
	
if __name__ == '__main__':
	if DEBUGGING:
		Launch()
	else:
		try:
			Launch()
		except:
			print("\nProgram Stopped Running")

