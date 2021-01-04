#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import pandas as pd


# In[2]:


#Loading Chrome
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
preferences = {"download.default_directory": os.getcwd()} # <- Change this for download directory
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome("chromedriver.exe", options=options)


# In[3]:


#Setting download link and downloading the file
driver.get("http://agence-prd.ansm.sante.fr/php/ecodex/telecharger/lirecis.php")


# In[4]:


#Loading downloaded txt as a csv
df = pd.read_csv("CIS.txt", sep='\t', encoding = "ISO-8859-1", index_col=False)
df.columns = ["FR dtbs #", "Product", "NFC", "Broad NFC", "MA Status", "Procedure type", "Commercialisation Status", "Some Other Number", "Some Other Number"]


# In[6]:


df.to_csv("France.csv", index=False)

