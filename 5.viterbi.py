from numpy.ma.core import asarray
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# dividindo a lista de viterbi entre Estado = 0 e Estado = 1

df = np.asarray(pd.read_csv('viterbi_list.csv'))
df_obitos = pd.read_csv('casos_obitos.csv')

E0 = []
E1 = []

for i in range(0, len(df)):
    if df[i] == 0:
        E0.append(df_obitos['new_deaths'][i])
    else:
        E1.append(df_obitos['new_deaths'][i])

# Boxplot de Óbito x Estado Fictício

def viterbi_1 ():
    
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False

    data = E0, E1
    fig = plt.boxplot(data, showfliers = False)
    
    plt.xlabel('Estados')
    plt.ylabel('Óbitos')
    plt.title('Sequência de Viterbi - MG 08/03/2020 - 27/07/2021')

    plt.show()

viterbi_1()

# print(max(df_obitos['date']))
# print(min(df_obitos['date']))
