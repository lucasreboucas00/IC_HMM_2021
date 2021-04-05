# Abrir CSV com Python

import pandas as pd

col_list = ['date', 'confirmed', 'deaths']

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

df = pd.read_csv('COVIDSP_21032021.csv')

print(df)
