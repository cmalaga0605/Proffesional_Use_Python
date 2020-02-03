#!/usr/bin/env python
# coding: utf-8

# In[50]:



import pandas as pd
name =['Crus','alex','George']
Salary= [4000,5000,5400]
combine = zip(name,Salary)

df = pd.DataFrame(data = combine,columns = ['name','Salary'])
df


# In[51]:


import numpy as np
#Created a conditional column
df['Big_Or_Small'] = np.where((df['Salary']>4000) & (df['name']== 'alex') , 'yes', 'no')
df


# In[52]:


#Create a conditional column
df['SalesA'] = np.where((df['Salary']>10),30,10)


# In[53]:


#Create a conditional column 
df['Total'] = df['Salary']+df['SalesA']


# In[74]:


#Filter by row in DataFrame
df[(df['Salary']>=400) & (df['name'].str.contains("s"))]


# In[66]:


#Filtered the rows where name contained s
df[df['name'].str.contains("s")]


# In[77]:


df['PointA'] = np.where((df['Big_Or_Small']== 'yes'),1,0)


# In[79]:


df['PointB'] = np.where((df['Big_Or_Small']== 'yes'),1,0)


# In[81]:


df['TotalPoint'] = df['PointA'] + df['PointB']


# In[82]:


df


# In[92]:


#Created a pivot table
T = pd.pivot_table(df, values =['TotalPoint','PointB'], index =['name','Salary'], aggfunc = 'sum') 
T


# In[102]:


#Subset of the pivot table
S = T.xs('alex',level=0)


# In[118]:


#Created An Excel File with multiple sheets
df1=pd.DataFrame(data=S)
df = pd.DataFrame(data=df)
writer = pd.ExcelWriter('Desktop/United.xlsx',engine='xlsxwriter')
df1.to_excel(writer,sheet_name='S')
df.to_excel(writer,sheet_name='T')
writer.save()

