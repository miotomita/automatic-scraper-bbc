#!/usr/bin/env python
# coding: utf-8

# <h1> in-class note</h1>
# <br>scraping
# <br>July 26, 2022

# In[14]:


import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# In[4]:


url = "https://www.bbc.com/"


# In[5]:


response = requests.get(url)
doc = bs(response.text)


# In[18]:


titles = doc.select(".media__title a")


# In[19]:


rows = []
for title in titles:
    row = {}
    # title
    row['title'] = title.text.strip()
    # link
    row['url'] = title['href']
    
    rows.append(row)
    
df = pd.DataFrame(rows)
df.head()


# In[17]:


df.to_csv("bbc.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:




