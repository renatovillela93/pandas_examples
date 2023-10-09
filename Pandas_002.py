#!/usr/bin/env python
# coding: utf-8

# # Comparing, Processing and Merging DataFrames
# 
# ## Goal
# 
# We will modify the IDs for the names of products, customers and stores, so our analyzes will be more intuitive in the future. To do this, we will create a data frame with all the details.
# 
# - We will use the merge method for this and, later if we want, we can get just the columns we want from the final dataframe.

# ### Creating our dataframes

# In[11]:


import pandas as pd

#sometimes we will need to change the encoding. Possible values to test:
#encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' or encoding='cp1252'
vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv('Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';')


#we will use the display to see all dataframes
display(vendas_df)
display(produtos_df)
display(lojas_df)
display(clientes_df)


# ### Let's remove the useless columns from cliente_df or just get the columns we want
.drop([coluna1, coluna2, coluna3]) -> remove the columns: column1, column2, column3
# In[13]:


# First option: using .drop
clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis = 1)

# Reading clients_df again
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';')

# Second option: resetting clients_df
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]
display(produtos_df)


# ### Now let's join the dataframes to have 1 single dataframe with everything "pretty"
new_dataframe = dataframe1.merge(dataframe2, on='coluna')
# - Note: The merge needs columns with the same name to work. If not, you need to change the column name with .rename
dataframe.rename({'coluna1': 'novo_coluna_1'})
# In[14]:


#joining the dataframes
vendas_df = vendas_df.merge(produtos_df, on = 'ID Produto')
vendas_df = vendas_df.merge(lojas_df, on = 'ID Loja')
vendas_df = vendas_df.merge(clientes_df, on = 'ID Cliente')

#displaying the final dataframe
display(vendas_df)


# In[15]:


#let's rename the email to make it clear that it is from the customer
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

#Checking if it worked
display(vendas_df)

