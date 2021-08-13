import pandas as pd

col_list = ['date', 'new_confirmed', 'new_deaths']
df = pd.read_csv('COVIDMG_ESTADO_20212707.csv', usecols = col_list)


print(df)

df.to_csv('casos_obitos.csv', index = False)