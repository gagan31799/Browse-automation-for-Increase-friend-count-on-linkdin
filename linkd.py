# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 01:50:12 2018

@author: Garg
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
import pprint

#userid = str(input("Enter email address or number with country code: "))
userid = "garg31799@gmail.com" 
#password = getpass.getpass('Enter your password:')
password="enter your password"
chrome_path = "c:\\users\\Garg\\Downloads\\chromedriver_win32\\chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.linkedin.com")
#driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="login-email"]""").send_keys(userid)
driver.find_element_by_xpath("""//*[@id="login-password"]""").send_keys(password)
driver.find_element_by_xpath("""//*[@id="login-submit"]""").click()
driver.get("https://www.linkedin.com/in/psuparn")
#connectionName = driver.find_element_by_class_name('visually-hidden').get_attribute('innerHTML')
#elem=driver.find_element_by_partial_link_text("urn%3Ali%3Acontrol%3Ad_flagship3_profile_view_base-topcard_view_all_connections")
#elem.click()

list1 = []
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    list1.append(elem.get_attribute("href"))
for i in list1:
    if "https://www.linkedin.com/search/results/people/?" in i:
        driver.get(i)
        break
driver.get("https://www.linkedin.com/search/results/people/?facetConnectionOf=%5B%22ACoAACVTQKABeBUBehhkPTx49QQS8iJm51E9Lm8%22%5D&facetNetwork=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page=56")
a=driver.page_source
count = 0
while("No results found." not in a):
    driver.get("https://www.linkedin.com/search/results/people/?facetConnectionOf=%5B%22ACoAACVTQKABeBUBehhkPTx49QQS8iJm51E9Lm8%22%5D&facetNetwork=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page="+str(count))
    a=driver.page_source
