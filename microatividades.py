# # Microatividades – DGT2823
#
# Leitura e exploração do conjunto de dados `dados.csv` com a biblioteca Pandas.

# ## Microatividade 1: ler um arquivo CSV com Pandas

import pandas as pd

# Lê o CSV informando o separador de colunas (;), a engine 'python' e o encoding
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

print(dados)

# ## Microatividade 2: criar um subconjunto de dados (3 colunas)

subconjunto = dados[['ID', 'Duration', 'Calories']]

print(subconjunto)

# ## Microatividade 3: configurar o número máximo de linhas exibidas

# Define o máximo de linhas exibidas como 9999
pd.set_option('display.max_rows', 9999)

print(dados.to_string())

# ## Microatividade 4: primeiras e últimas N linhas

print('Primeiras 10 linhas:')
print(dados.head(10))

print()
print('Últimas 10 linhas:')
print(dados.tail(10))

# ## Microatividade 5: informações gerais do conjunto de dados

# Informações gerais: colunas, tipos, nulos e memória utilizada
dados.info(memory_usage='deep')

print()
print('Total de linhas :', dados.shape[0])
print('Total de colunas:', dados.shape[1])
print()
print('Quantidade de nulos por coluna:')
print(dados.isnull().sum())
print()
print('Tipo de dado de cada coluna:')
print(dados.dtypes)
print()
print('Memória utilizada (bytes):', dados.memory_usage(deep=True).sum())
