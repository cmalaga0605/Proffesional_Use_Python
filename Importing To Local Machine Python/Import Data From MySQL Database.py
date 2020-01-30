#!/usr/bin/env python
# coding: utf-8

# In[20]:


get_ipython().system('pip install sqlalchemy')
get_ipython().system('pip install pymysql')
import pymysql

engine = sqlalchemy.create_engine('mysql+pymysql://root:2217546@Cmjs@localhost:3306/usimagingnetwork')


# In[21]:


df = pd.read_sql_table('employee',engine)
df


# Note you need to get the database URL
# dialect+driver://username:password@host:port/database
