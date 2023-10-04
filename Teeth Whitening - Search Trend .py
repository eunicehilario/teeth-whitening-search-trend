#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()


# In[2]:


trends.build_payload(kw_list=["Teeth Whitening"])
data = trends.interest_by_region()
data = data.sort_values(by="Teeth Whitening", ascending=False)
data = data.head(10)
print(data)


# In[3]:


data.reset_index().plot(x="geoName", 
                        y="Teeth Whitening", 
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()


# In[4]:


data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Teeth Whitening'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['Teeth Whitening'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Teeth Whitening', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()


# In[ ]:





# In[ ]:




