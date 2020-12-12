#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import requests
import pprint
import pyperclip


# In[2]:


html=urlopen("https://www.bda.bg/images/stories/documents/bdias/A-1.htm")
soup=BeautifulSoup(html, "lxml")


# In[ ]:





# In[3]:


# table = soup.findAll('table')[0]
# rows = table.findAll('tr')

# first_columns = []
# third_columns = []
# for row in rows:
#     first_columns.append(row.findAll('td')[0].contents)


# In[ ]:





# In[4]:


unwanted = soup.find_all(class_=["xl24", "xl71"])
for span in unwanted:
    span.decompose()


# In[ ]:





# In[5]:


rowsa = soup.select('table tr td:nth-of-type(1)')
rowsb = soup.select('table tr td:nth-of-type(2)')

A = []
B = []

for row in rowsa:
    A.append(row.text)
for row in rowsb:
    B.append(row.text)
    
A = pd.Series(A, name="Product")
A = A.str.replace("\r", "")
A = A.str.replace("\n", "")
A = A.str.replace("\xa0", "")
A.replace('', np.nan, inplace=True)
first_idx = A.first_valid_index()
last_idx = A.last_valid_index()
A = A.loc[first_idx:last_idx]
#A.dropna(inplace=True)
#A.reset_index(drop=True)

B = pd.Series(B, name="Strength")
B = B.str.replace("\r", "")
B = B.str.replace("\n", "")
B = B.str.replace("\xa0", "")
B.replace('', np.nan, inplace=True)
first_idx = B.first_valid_index()
last_idx = B.last_valid_index()
B = B.loc[first_idx:last_idx]
#B.dropna(inplace=True)
#B.reset_index(drop=True)


# In[6]:


X = pd.concat([A.reset_index(drop=True), B.reset_index(drop=True)], axis=1)


# In[7]:


X.to_csv("TEST1.csv", index=False)

