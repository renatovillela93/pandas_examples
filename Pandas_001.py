#!/usr/bin/env python
# coding: utf-8

# # DataFrame
# 
# 
# ## Summary
# 
# It's like a table.
# 
# - Columns work "like dictionary keys"
# - Lines work "like lists"
# 
# ## Operation
We have a dataframe called sales_df

sales_df['coluna_x'] -> a list with the values of column_x (in dataframe format, it is a dataframe with only 1 column)
sales_df[0] -> IT DOESN'T WORK LIKE THIS FOR DATAFRAMES
sales_df[:3] -> takes up to index line 3 of the dataframe
sales_df[['coluna_x', 'coluna_y', 'coluna_z']] -> creates a new dataframe with the columns column_x, column_y and column_z
sales_df['coluna_x'][0] -> gets the itemd the 1st line of the column column_x
# - Let's read a real file, with the Sales Database of the Company "Contoso"

# In[3]:


import pandas as pd

vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';')

vendas_df


# In[4]:


vendas_df[:3]


# In[5]:


vendas_df[['Data da Venda', 'Data do Envio', 'ID Produto']]


# ## Application

# - The 1st step of all Data Analysis is to understand what exists in your database
# 
# We will use .info() for this

# In[6]:


vendas_df.info()


# - Let's now create a list of Customers

# In[8]:


clientes_df = vendas_df['ID Cliente']
clientes_df


# - Let's now create a list with the products and their sales quantities, in case we want to analyze just the products (regardless of date or customer)

# In[9]:


produtos_quantidades_df = vendas_df[['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']]
produtos_quantidades_df

