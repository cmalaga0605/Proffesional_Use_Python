#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pyodbc 
import pandas as pd
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DB039O6\SQLEXPRESS;'
                      'Database=USImagingFiles;'
                      'Trusted_Connection=yes;')
df = pd.read_sql_query('SELECT * FROM TestRun',conn)
df

