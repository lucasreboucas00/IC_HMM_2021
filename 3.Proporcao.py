import pandas as pd
import matplotlib.pyplot as plt

data_ref = 7, 14, 21 # considerando referência de 7, 14 e 21 dias 

df = pd.read_csv('obs_covid.csv') 

l1 = []
l2 = []
l3 = []


for j in (data_ref):

    for i in range(len(df)): 

        if df['observation_' + str(j)][i] == 0:
            l1.append(df['new_deaths'][i])

        if df['observation_' + str(j)][i] == 1:
            l2.append(df['new_deaths'][i])

        if df['observation_' + str(j)][i] == 2:
            l3.append(df['new_deaths'][i])


    def image1():

        plt.rcParams['axes.spines.top'] = False
        plt.rcParams['axes.spines.right'] = False

        #lista_classe_2 = [12, 15, 20...]

        data = (l1, l2, l3)
        a = plt.boxplot(data, showfliers = False)


        plt.xlabel('Classe')
        plt.ylabel('Óbitos')
        plt.title('Relação Óbitos x Classe - Simulação ' + str(j) + ' dias')

        plt.show()

    image1()
    
