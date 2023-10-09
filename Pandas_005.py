#!/usr/bin/env python
# coding: utf-8

# # Adding Columns, Modifying Columns and Values

# ### Let's get our dataframe again

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


# In[5]:


vendas_df.info()
# You need to modify the Sale Date and Shipping Date for the datetype


# ### Now, what if we want to add a column with the month, day and year of each sale (and not just the full date)

# In[13]:


vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format="%d/%m/%Y")
vendas_df['Ano da Venda'] = vendas_df['Data da Venda'].dt.year
vendas_df['Mês da Venda'] = vendas_df['Data da Venda'].dt.month
vendas_df['Dia da Venda'] = vendas_df['Data da Venda'].dt.day

display(vendas_df)
vendas_df.info()


# ### And now, if we want to modify a specific value, how do we do it? Let's import the product base again

# In[1]:


novo_produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
display(novo_produtos_df.head())
#notice .head() to only get the first values, this is quite common to use to get a view of what the data is


# ### We need to talk about 2 methods:
#      1. loc - allows you to get a line according to its index. It gives an error if it does not find the index. This is interesting especially when the index is relevant information instead of just the index number or when we want to get a specific line from the dataframe (instead of going from the beginning of the dataframe to line 5, for example).
#          We can also use loc[row_index, column_index] to access a specific value and modify it.
#      2. iloc - sees the dataframe as rows and columns and can get the value with a row number and a column number. Note that it does not analyze the value of the row and column index, only the position matters.
#          Usage: iloc[row_num, column_num]
