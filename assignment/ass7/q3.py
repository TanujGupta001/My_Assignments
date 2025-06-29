import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
print(df)
print('----------------------------')
print(df.info())
print('----------------------------')
print(df.describe(include='all'))
print('----------------------------')
print(df.isnull().sum())
print('----------------------------')
print(df.tail())
print('----------------------------')
print(df.to_string())
print('----------------------------')
grouped = df.groupby(['Gender', 'Age']).sum()
print('----------------------------')
print(grouped)