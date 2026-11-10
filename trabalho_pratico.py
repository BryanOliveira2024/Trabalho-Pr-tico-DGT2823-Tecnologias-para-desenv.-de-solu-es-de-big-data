# # Trabalho Prático – DGT2823
#
# Limpeza de um conjunto de dados com Python e Pandas.

# ## Passos 1 a 4: ler o CSV e atribuir a uma variável

import numpy as np
import pandas as pd

# O arquivo usa ';' como separador e contém valores inválidos que serão tratados
df = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# ## Passo 5: verificar se os dados foram importados corretamente

# 5a) Informações gerais
df.info()

print()
# 5b) Primeiras e últimas N linhas
print('Primeiras 10 linhas:')
print(df.head(10))
print()
print('Últimas 10 linhas:')
print(df.tail(10))

# ## Passo 6: copiar o conjunto de dados original

df2 = df.copy()

# ## Passo 7: substituir os valores nulos de 'Calories' por 0

df2['Calories'] = df2['Calories'].fillna(0)

print(df2)

# ## Passo 8: tratar os valores nulos de 'Date'

# 8a) Substitui os nulos de 'Date' por '1900/01/01'
df2['Date'] = df2['Date'].fillna('1900/01/01')

# 8b) Confere a mudança
print(df2)

# 8c) Tenta transformar 'Date' em datetime: ocorre um erro de formato
try:
    df2['Date'] = pd.to_datetime(df2['Date'])
except ValueError as erro:
    print('ERRO esperado:')
    print(erro)

# ## Passo 9: corrigir o valor '1900/01/01'

# 9a) Troca '1900/01/01' por NaN
df2['Date'] = df2['Date'].replace('1900/01/01', np.nan)

# 9b) Tenta novamente a transformação: surge um novo erro (valor 20201226)
try:
    df2['Date'] = pd.to_datetime(df2['Date'])
except ValueError as erro:
    print('ERRO esperado:')
    print(erro)

# 9c) Confere o conjunto de dados
print()
print(df2)

# ## Passo 10: tratar o valor '20201226' (replace + to_datetime)

# O valor 20201226 é uma string fora do padrão. Passa para o mesmo formato dos demais.
df2['Date'] = df2['Date'].replace('20201226', "'2020/12/26'")

print(df2.loc[24:28])

# ## Passo 11: transformar toda a coluna 'Date' em datetime

df2['Date'] = pd.to_datetime(df2['Date'])

print(df2)
print()
print(df2.dtypes)

# ## Passo 12: remover os registros com valores nulos

# Apenas a coluna 'Date' ainda possui nulo (linha 22)
df2 = df2.dropna()

# ## Passo 13: verificar as transformações

print(df2)
print()
df2.info()
print()
print('Nulos restantes:', int(df2.isnull().sum().sum()))
print('Total de linhas:', df2.shape[0])
