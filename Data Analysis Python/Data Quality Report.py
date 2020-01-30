#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
Location = 'Desktop/health-insurance/states.csv'
df = pd.read_csv(Location)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df.head(10)


# In[16]:


datatypes=pd.DataFrame(df.dtypes,columns=['DataType']) #datatype for each column

datatypes


# In[20]:


missing_data_values=pd.DataFrame(df.isnull().sum(),columns=['Missing Values']) #Count missing values per column

missing_data_values


# In[24]:


present_values=pd.DataFrame(df.count(),columns=['Present Values']) #values in each columns

present_values


# In[26]:


unique_values_count=pd.DataFrame(columns=['Unique Values Count']) #Number of unique values
for i in list(df.columns.values):
    unique_values_count.loc[i]=[df[i].nunique()]
unique_values_count 


# In[32]:


minimum_values=pd.DataFrame(columns=['Minimum Values']) #Minimum Values
for i in list(df.columns.values):
    minimum_values.loc[i]=[df[i].min()]
minimum_values


# In[33]:


Maximum_values=pd.DataFrame(columns=['Max Values']) #Max values
for i in list(df.columns.values):
    Maximum_values.loc[i]=[df[i].max()]
Maximum_values


# In[35]:


pd.concat([datatypes,missing_data_values,present_values,unique_values_count,minimum_values,Maximum_values],axis=1)#full report

