import pandas as pd

df = pd.read_csv('../data/interim/1_cleaned.csv')

#print(df.dtypes)

# Classification values ready for categorical conversion
df['Classification'] = df['Classification'].replace({
	'Park Trail': 'PT',
    'Regional Trail': 'RT'
})

# Plowed values ready for boolean conversion
df['Plowed'] = df['Plowed'].apply(lambda x: True if str(x).strip().lower() == 'yes' else False)

#print(df['Winter_Use'].value_counts())
#print(df['Summer_Use'].value_counts())

# Length values from m to ft 
if 'Length_m' in df.columns:
	df['Length_ft'] = df['Length_m'] * 3.28084
	df = df.drop(columns=['Length_m'])


#Round float values to 2 decimal places
if 'Length_ft' in df.columns:
	df['Length_ft'] = df['Length_ft'].round(2)
	
if 'Width_ft' in df.columns:
	df['Width_ft'] = df['Width_ft'].round(2)

df.to_csv('../data/interim/2_cleaned.csv', index=False)


