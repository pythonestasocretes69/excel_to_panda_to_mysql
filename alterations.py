import numpy as np
import pandas as pd

df = pd.read_csv('stock_report.csv')

#print(df)
print(df.describe())


# this will reindex the panda
df.index = df['Date']
df = df.drop('Date',axis=1)
print(df)

#creation of new csv file will again shift the index

