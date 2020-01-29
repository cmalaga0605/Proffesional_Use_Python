#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np 
import pdpipe as pdp 

Location = 'Desktop/health-insurance/states.csv'
states = pd.read_csv(Location)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
states.head(20)

