#!/usr/bin/env python
# coding: utf-8

# # Exporting from the DataFrame to a csv
# 
# ### After modifying a DataFrame, or even creating one, we can often export that dataframe to a csv
# 
# With pandas this is quite simple:
# 
# dataframe.to_csv('nome_do_arquivo.csv', sep=',')

# ### Reading a DataFrame, modifying it and exporting

# In[15]:


import pandas as p
import chardet

# Discovering the encoder of files (UnicodeDecodeError)

# Detect the encoding of a CSV file
with open('Contoso - Cadastro Produtos.csv', 'rb') as f:
    result = chardet.detect(f.read())

print(result['encoding'])

with open('Contoso - Lojas.csv', 'rb') as f:
    result = chardet.detect(f.read())

print(result['encoding'])

with open('Contoso - Clientes.csv', 'rb') as f:
    result = chardet.detect(f.read())

print(result['encoding'])


# In[18]:


# importing the files
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';', encoding='UTF-8-SIG')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';', encoding='UTF-8-SIG')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';', encoding='UTF-8-SIG')

# clearing only the columns we want
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# merging and renaming the dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})
display(vendas_df)


# In[20]:


# now let's create the csv
vendas_df.to_csv('new_sales_2017.csv',sep=';')


# ### Creating a dictionary, transforming the dictionary into a DataFrame and exporting to csv

# In[24]:


# Creating Dictionary
sales_products = {'iphone': [558147, 951642], 'galaxy': [712350, 244295], 'ipad': [573823, 26964], 'tv': [405252, 787604], 'máquina de café': [718654, 867660], 'kindle': [531580, 78830], 'geladeira': [973139, 710331], 'adega': [892292, 646016], 'notebook dell': [422760, 694913], 'notebook hp': [154753, 539704], 'notebook asus': [887061, 324831], 'microsoft surface': [438508, 667179], 'webcam': [237467, 295633], 'caixa de som': [489705, 725316], 'microfone': [328311, 644622], 'câmera canon': [591120, 994303]}

# Transforming to DataFrame
sales_products_df = pd.DataFrame.from_dict(sales_products, orient='index')
sales_products_df = sales_products_df.rename(columns = {0:'Sales 2019', 1:'Sales 2020'})

display(sales_products_df)

# Exporting 
sales_products_df.to_csv('new_sales_products.csv', sep=',', encoding='latin1')

