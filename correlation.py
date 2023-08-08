import pandas as pd

# get the table
location = 'Scores.xlsx'
df = pd.read_excel(location)
description = df.describe()

MMean = description.loc['mean', 'Mathematics']
PMean = description.loc['mean', 'Physics']
CMean = description.loc['mean', 'Chemistry']
TMean = description.loc['mean', 'Total']

# covariance
cov = 0
for i in df.index:
    term = (TMean - df.loc[i, 'Total']) * (MMean - df.loc[i, 'Mathematics'])
    cov += term
cov /= len(df.index)
print('cov=', cov)
corr = cov / (description.loc['std', 'Mathematics'] * description.loc['std', 'Total'])
print('corr=', corr)
