# basic code to activate the selenium driver and get corresponding page source

import selenium
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

path = "/home/vipul/Downloads/chromedriver_linux64/chromedriver"

url = "Your fav website"

driver = webdriver.Chrome(path)
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

print(soup)

driver.close()
