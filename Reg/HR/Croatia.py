#!/usr/bin/env python
# coding: utf-8

# In[8]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os


# In[9]:


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
preferences = {"download.default_directory": os.getcwd()} # <- Change this for download directory
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome("chromedriver.exe", options=options)


# In[10]:


#Clicking expand
driver.get("https://www.halmed.hr/en/Lijekovi/Baza-lijekova/")
#button= driver.find_elements_by_class_name("btn_wrapp")
button = driver.find_elements_by_xpath("//input[@type='submit' and @value='search']")[0]
button.click()
page_source = driver.page_source


# In[11]:


#Clicking download
button = driver.find_elements_by_xpath("//a[@class='spremi_rezultate' and @id='btn_spremi_rezultate']")[0]
button.click()


# In[6]:




