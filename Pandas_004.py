#!/usr/bin/env python
# coding: utf-8

# # Filtering information in dataframes
# 
# 
# ## Summary
# 
# One of pandas' great potential is to treat conditions.
# 
# And the way we analyze conditions in the dataframe is different from what we've done so far in the course, let's see how it works.

# - Preparing the databases

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


# ### First, let's apply a function normally. What % of sales were returned?
# 
# - To do this, we will add the quantities in the corresponding columns. Remember, the % will be: Total Returned / Total Sold.

# In[4]:


qtde_vendida = vendas_df['Quantidade Vendida'].sum()
qtde_devolvida = vendas_df['Quantidade Devolvida'].sum()

print('{:.2%}'.format(qtde_devolvida/qtde_vendida))


# ### Now, if we want to do the same analysis for just 1 store. We want to filter only items from the Contoso Europe Online Store and know the return % from that store.
# 
# - For this, we will need to filter. The way to filter in dataframes is a "simple" comparison

# In[5]:


vendas_loja_contoso = vendas_df[vendas_df['ID Loja'] == 306]
display(vendas_loja_contoso)


# In[6]:


qtde_vendida_contoso = vendas_loja_contoso['Quantidade Vendida'].sum()
qtde_devolvida_contoso = vendas_loja_contoso['Quantidade Devolvida'].sum()

print('{:.2%}'.format(qtde_devolvida_contoso/qtde_vendida_contoso))


# ### Let's do it in 2 steps to understand exactly what is happening.

# In[10]:


#vendas_loja_contoso = vendas_df[vendas_df['ID Loja'] == 306]

loja306 = vendas_df['ID Loja'] == 306
display(loja306)

vendas_loja_contoso2 = vendas_df[loja306]
display(vendas_loja_contoso2)


# ### Challenge: what if I wanted to create a table with only sales from the Contoso Europe Online Store that had no returns. I want to create this table and know how many sales there are.
# 
# - Note that in this case there are 2 conditions, how do we do this?

# In[15]:


#all together
vendas_loja_contosoeuropeonline = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]
display(vendas_loja_contosoeuropeonline)


# In[16]:


#separate
vendas_loja_contosoeuropeonline = vendas_df[vendas_df['ID Loja'] == 306] #Selecting Contoso Europe Online store
vendas_loja_contosoeuropeonline = vendas_df[vendas_df['Quantidade Devolvida'] == 0] #Selecting sales without returns

display(vendas_loja_contosoeuropeonline)

