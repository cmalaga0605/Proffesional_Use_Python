#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd 
Location = 'Desktop/Ex.csv'
df=pd.read_csv(Location)


# In[82]:


df.dtypes


# In[83]:


df.fillna(' ')


# In[84]:


df.rename(columns={'State':'Yh','Employer Health Insurance Coverage (2015)':'G'},inplace=True)


# In[85]:


df['G']=df['G'].astype('float')


# In[86]:


df.head(10)


# In[88]:


import pymysql
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:2217546@Cmjs@localhost:3306/usimagingnetwork')
df.to_sql(
    name='df_test',
    con=engine,
    index=False,
    if_exists='append'
)    


# In[ ]:




