#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import re
import requests
import yfinance as yf
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#get AAstocks HSI component page
soup = BeautifulSoup(requests.get('http://www.aastocks.com/en/stocks/market/index/hk-index-con.aspx').content)

#yfinance hk ticker pattern
yf_tick_pattern = re.compile(r'[0-9]{4}\.hk')

#get hsi tickers from soup
hsi_tickers = [yf_tick_pattern.findall(line.text.lower())[0] for line in soup.find_all('a',attrs = {'class':'a14 cls'})]

#grab data from yf
start_date,end_date = '2018-01-01','2019-01-01'
data = yf.download(hsi_tickers,start_date,end_date)


# In[6]:


#add yesterday's date to each day's data
#dates = data.index.tolist()
#yestermap = np.array([dates[1:],dates[0:-1]]).transpose()#
#yesterdf = pd.DataFrame(yestermap,columns = ['Date','Yesterdate'])
#yesterdf.set_index('Date',inplace=True)
#close_data = data.Close.join(yesterdf, on='Date')
#close_data[['0001.HK']].pct_change()
#returns = close_data.drop('Yesterdate',axis=1).subtract(close_data.set_index('Yesterdate')).div(close_data.drop('Yesterdate',axis=1))


# In[3]:


returns = data['Adj Close'].pct_change()


# In[6]:


tickers = ['0001.HK','0002.HK','0003.HK']


# In[ ]:





# In[7]:


w = [1/len(tickers)]*len(tickers)


# In[24]:


init_cap = 100


# In[25]:


entry_date = '2018-01-03'


# In[31]:


close = data['Adj Close']


# In[60]:


wgt_df = pd.DataFrame(w,tickers,columns=['wgt'])
returns[tickers].dot(wgt_df).cumsum().plot(figsize=(12,6))


# In[61]:


sns.lmplot(data=returns[tickers],x='0001.HK',y='0002.HK')


# In[46]:


monthly_last_week = returns.groupby(returns.index.month).tail(5)
monthly_last_week.groupby(monthly_last_week.index.month).sum().rank(axis=1)


# In[47]:


monthly_last_week.groupby(monthly_last_week.index.month).sum()[['0883.HK']]

