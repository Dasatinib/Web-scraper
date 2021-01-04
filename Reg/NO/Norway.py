#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os


# In[2]:


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
preferences = {"download.default_directory": os.getcwd()} # <- Change this for download directory
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome("chromedriver.exe", options=options)


# In[3]:


driver.get("https://www.legemiddelsok.no/")
button = driver.find_elements_by_xpath("/html/body/form/div[4]/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/a")[0]
button.click()

