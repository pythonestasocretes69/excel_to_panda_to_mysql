import pandas as pd

# get the table
location = 'Scores.xlsx'
df = pd.read_excel(location)
description = df.describe()

# menue addidng
menue =  df.columns()
primary_i = int(input ('Enter index of primary factor' + str(menue))) 
secondary_i = int(input ('Enter index of secondary factor' + str(menue))) 
primary = menue.pop(primary_i)
secondary = menue.pop(secondary_i)
PMean = description.loc('avg',primary)
SMean = description.loc('avg',secondary)

# covariance
cov = 0
for i in df.index:
    term = (PMean - df.loc[i, primary]) * (SMean - df.loc[i, secondary])
    cov += term
cov /= len(df.index)
print('cov=', cov)
corr = cov / (description.loc['std', secondary] * description.loc['std', primary])
print('corr=', corr)
