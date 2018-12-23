# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 01:50:12 2018

@author: Garg
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pprint
from selenium.webdriver.support.ui import WebDriverWait

#userid = str(input("Enter email address or number with country code: "))

#password = getpass.getpass('Enter your password:')
userid,password="garg31799@gmail.com","papa@papa"
chrome_path = "c:\\users\\Garg\\Downloads\\chromedriver_win32\\chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.linkedin.com")
#driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="login-email"]""").send_keys(userid)
driver.find_element_by_xpath("""//*[@id="login-password"]""").send_keys(password)
driver.find_element_by_xpath("""//*[@id="login-submit"]""").click()
driver.get("https://www.linkedin.com/in/psuparn/")


list1 = []
elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    list1.append(elem.get_attribute("href"))
for i in list1:
    if "https://www.linkedin.com/search/results/people/?" in i:
        driver.get(i)
        break
list2=[]

a=driver.page_source
count = 1
while("No results found." not in a):
    driver.get("https://www.linkedin.com/search/results/people/?facetConnectionOf=%5B%22ACoAACVTQKABeBUBehhkPTx49QQS8iJm51E9Lm8%22%5D&facetNetwork=%5B%22F%22%2C%22S%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH&page="+str(count))
    elems1 = driver.find_elements_by_xpath("//a[@href]")
    for elem2 in elems1:
        list2.append(elem2.get_attribute("href"))
    a=driver.page_source
    count=count+1
    if count==:
        break;
    
list3=[]
for p in list2:
    if "https://www.linkedin.com/in/" in p:
        list3.append(p)
c=set(list3)
list3=list(c)
list3.insert(0,"https://www.linkedin.com/in/varun-bagga-aa724151/")
list3.insert(0,"https://www.linkedin.com/in/ballardrules/")
list3.insert(0,"https://www.linkedin.com/in/kalie-zuanich-651ab55a/")
list3.insert(0,"https://www.linkedin.com/in/ramonpizarro/")
for i in list3:
    driver.get(i)
    x=driver.find_element_by_class_name("pv-s-profile-actions__label")
    x.click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-primary-large ml1']"))).click()
