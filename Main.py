

import pandas as pd

df = pd.read_csv('sales_data_sample.csv')

print(df.head())
print(df.info())
# removi os nulos destas colunas
df = df.dropna(subset=['QUANTITYORDERED','PRICEEACH','ORDERDATE','PRODUCTLINE'])
print(df.info())
# convertendo a coluna ORDERDATE para dados pois ela estava em str
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
print(df.info())
# criei a coluna REVENUE
df['REVENUE'] = df['QUANTITYORDERED'] * df['PRICEEACH']
print(df.info())
# criei a coluna MONTH, extraindo o mês da coluna ORDERDATE
df['MONTH'] = df['ORDERDATE'].dt.month
print(df.head())
df.to_csv('vendas_tratado2.csv', index=False, sep=';', decimal=',')


