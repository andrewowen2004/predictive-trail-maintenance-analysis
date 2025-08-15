import pandas as pd

df = pd.read_csv('../data/interim/1_cleaned.csv')

#print(df.dtypes)

# Classification values ready for categorical conversion
df['Classification'] = df['Classification'].replace({
	'Park Trail': 'PT',
    'Regional Trail': 'RT'
})

# Plowed Values ready for boolean conversion
df['Plowed'] = df['Plowed'].apply(lambda x: True if str(x).strip().lower() == 'yes' else False)



#df.to_csv('../data/interim/2_cleaned.csv', index=False)


