import pandas as pd

df = pd.read_csv('../data/interim/2_cleaned.csv')

print(df.dtypes)

type_map = {
	'Classification': 'category',
	'Park': 'category',
	'City': 'category',
	'Surface_Type': 'category',
	'Width_ft': 'float',
	'Summer_Use': 'category',
	'Winter_Use': 'category',
	'Plowed': 'bool',
	'Trail_Name': 'string',
	'Length_ft': 'float'
}
for col, dtype in type_map.items():
	if col in df.columns:
		df[col] = df[col].astype(dtype)

print(df.dtypes)

df.to_csv('../data/interim/3_cleaned.csv', index=False)
