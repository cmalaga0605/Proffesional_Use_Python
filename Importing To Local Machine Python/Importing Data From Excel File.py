#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
Location = 'Documents/Excel Reports/supermarket_sales -.xlsx' # Location of data on the machine
df = pd.read_excel(Location) #Create Dataframe 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df.head() #Print first 5 rows of data

