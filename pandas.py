pandas.read_csv()

import pandas as pd

df = pd.read_csv('data/folder/namafile.csv')
print(df.head())

df = pd.read_csv('contoh.csv', sep=':', header=0, index_col='nama')
print(df.head())