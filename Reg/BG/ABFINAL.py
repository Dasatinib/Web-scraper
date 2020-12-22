#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests


# In[11]:


html=urlopen("https://www.bda.bg/images/stories/documents/bdias/drugs2_list2_1.htm")
soup=BeautifulSoup(html, 'html.parser')
link_list_A=["https://www.bda.bg/images/stories/documents/bdias/5-1.htm"]

for link in soup.find_all("a"):
    temp=link.get("href")
    link_list_A.append(temp)

del link_list_A[len(link_list_A)-1]
del link_list_A[1]


# In[12]:


open("output_A.html","w+")

urls = link_list_A
#scrape elements
for url in urls:
    response = requests.get(url)
    soup1 = BeautifulSoup(response.content, 'html.parser').select('table tr:nth-of-type(n+5)')
#    soup1 = soup1.select('table tr:nth-of-type(n+7)')
    with open("output_A.html", "a+", encoding='utf-8') as file:
        file.write("<table>\n")
        file.write(str(soup1))
        file.write("\n</table>")
        
soup_A = BeautifulSoup(open("output_A.html", encoding='UTF-8'), 'html.parser')


# In[11]:


rowsa = soup_A.select('table tr td:nth-of-type(1)')
rowsb = soup_A.select('table tr td:nth-of-type(2)')

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

B = pd.Series(B, name="Strength and Form")
B = B.str.replace("\r", "")
B = B.str.replace("\n", "")
B = B.str.replace("\xa0", "")
B.replace('', np.nan, inplace=True)
first_idx = B.first_valid_index()
last_idx = B.last_valid_index()
B = B.loc[first_idx:last_idx]

output_A = pd.concat([A.reset_index(drop=True), B.reset_index(drop=True)], axis=1)
output_A = output_A.dropna(how='all')

output_A.to_csv("Bulgarian list of MAs.csv", index=False)

