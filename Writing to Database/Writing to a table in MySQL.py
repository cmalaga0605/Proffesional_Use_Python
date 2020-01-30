#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install sqlalchemy
get_ipython().system('pip install pymysql')
import pymysql

engine = sqlalchemy.create_engine('mysql+pymysql://root:2217546@Cmjs@localhost:3306/usimagingnetwork')


# In[ ]:


df = pd.read_sql_table('employee',engine)
df


# In[ ]:


query = '''
SELECT customers.name,customers.phone_number,orders.name,orders.amount
FROM customers INNER JOIN orders
ON customers.id = orders.customers_id
'''
df = pd.read_sql_query(query,engine)
df


# In[ ]:


df = pd.read_csv('Customer.csv')
df


# In[ ]:


#you can rename columns
df.rename(columns={
    'Customer Name':'name',
    'Customer Phone':'Phone'
},inplace = True)
df


# In[ ]:


#Writing to the table
df.to_sql(
    name='Customers',
    con=engine,
    index = False,
    if_exists='append'
)

