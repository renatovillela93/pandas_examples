#!/usr/bin/env python
# coding: utf-8

# # Summaries and a little Visualization in pandas
# 
# 
# ## Summary
# 
# Let's see some methods to analyze our tables (dataframes)
# 
# Furthermore, we will use the standard pandas graph plots, but in the DataScience project we will see more beautiful and also very practical ones.
# 
# NOTE: Pandas uses matplotlib (which we saw in the "modules and libraries" section) to plot graphs.<br>
# If you want to customize more than the pandas default, import matplotlib and use matplotlib methods

# - Preparing the databases (what we did in the last class)

# In[2]:


import pandas as pd
#importing the files
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

#cleaning only the columns we want
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

#merging and renaming dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})
display(vendas_df)


# ### Which customer has purchased the most times?
# 
# - We will use the .value_counts() method to count how many times each Dataframe value appears
# - We will use the .plot() method to display a graph

# In[13]:


frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
#display(customer_frequency)

frequencia_clientes[:5].plot(figsize=(20,5))


# ### Which store sold the most?
# 
# - We will use .groupby to group our dataframe, according to what we want (adding the sales quantities, for example)

# In[23]:


vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
display(vendas_lojas[:5])


# - Now we need to get the highest value. We have 2 ways:
#      1. Sort the dataframe in descending order of Quantity Sold
#          - .sort_values method
#      2. Get the highest value directly
#          - .max() and .idxmax() methods

# In[27]:


#ordering the dataframe
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending = False)
display(vendas_lojas[:5])

#we can plot it on a graph
vendas_lojas[:5].plot(figsize=(15,5), kind='bar')


# In[29]:


#taking the largest value and index
maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()

print(melhor_loja, maior_valor)


# ### Which product sold the least?
# 
# - We already have a list created for this, just check the end of the list (since it is ordered) or use the methods:
#      1.min()
#      2. idxmin()

# In[32]:


#Directly from sales_stores
vendas_lojas[-1:]


# In[33]:


#taking the largest value and index
menor_valor = vendas_lojas['Quantidade Vendida'].min()
pior_loja = vendas_lojas['Quantidade Vendida'].idxmin()

print(pior_loja, menor_valor)

