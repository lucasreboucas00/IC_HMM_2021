# Abrir CSV com Python
# Histograma de casos e mortes

import pandas as pd
import matplotlib.pyplot as plt


def histogram(dataframe, x, bins_quantity):
    plt.title('Histogram of {}' .format(x))
    plt.xlabel('{}' .format(x))
    plt.ylabel('Absolute Frequency')
    plt.hist(dataframe[x], bins_quantity, rwidth=0.7)
    plt.show()


col_list = ['date', 'confirmed', 'deaths', 'estimated_population']

pd.set_option('display.max_columns', None)  # não truncar colunas
#  pd.set_option('display.max_rows', None)   # não truncar linhas

df = pd.read_csv('COVIDSP_21032021.csv', usecols=col_list, index_col='date')

population = df['estimated_population'][0]  # extrai ~quantidade de habitates

daily_cases = []  # lista para manipular valores
df['daily_cases'] = 0  # valor no Data Frame

daily_deaths = []
df['daily_deaths'] = 0

for i in range(len(df) - 1):
    daily_cases.append(df['confirmed'][i] - df['confirmed'][i + 1])
    daily_deaths.append(df['deaths'][i] - df['deaths'][i + 1])

    df['daily_cases'][i] = daily_cases[i]
    df['daily_deaths'][i] = daily_deaths[i]
    # quant casos diários = confirmados [atual] - confirmado[atual-1]

# média móvel de casos por 14 dias

ma14_cases = []
df['ma14_cases'] = 0

for i in range(len(df) - 13):
    mac = 0  # mmc = média móvel de casos

    for j in range(i, i + 14):
        mac = float(mac + (df['daily_cases'][j] / 14))

    ma14_cases.append(round(mac))
    df['ma14_cases'][i] = ma14_cases[i]

df = df.drop(columns=['confirmed', 'deaths', 'estimated_population'])

#  print(df)

histogram(df, 'daily_cases', 14)
histogram(df, 'daily_deaths', 7)
