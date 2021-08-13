import numpy as np
import pandas as pd


df = pd.read_csv('casos_obitos.csv')
data_ref = 7, 14, 21 # considerando referência de 7, 14 e 21 dias 
pd.set_option('display.max_rows', None)   # não truncar linhas


# Criando colunas de referências obitos x casos para data_ref

for j in (data_ref):

    df['cases_' + str(j)] = 0
    
    for i in range(len(df) - j):
        df['cases_' + str(j)][i] = df['new_confirmed'][i + j]


# Classicando a quantidade de casos do dia em 3 possíveis classes 0, 1, 2

for j in (data_ref):
    
    df['observation_' + str(j)] =  0

    for i in range(len(df)):
        
        if df['cases_' + str(j)][i] <= np.quantile(df['cases_' + str(j)], 0.25):
            
           df['observation_' + str(j)][i] = 0

        if  np.quantile(df['cases_' + str(j)], 0.25) < df['cases_' + str(j)][i] <= np.quantile(df['cases_' + str(j)], 0.75):
            
           df['observation_' + str(j)][i] = 1

        if np.quantile(df['cases_' + str(j)], 0.75) < df['cases_' + str(j)][i]:
            
           df['observation_' + str(j)][i] = 2
        

print(df)

df.to_csv('obs_covid.csv')



