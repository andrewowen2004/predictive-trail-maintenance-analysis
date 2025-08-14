import pandas as pd

df = pd.read_csv('../data/interim/0_cleaned.csv')

df = df.rename(columns={
	'TRPDClassification': 'Classification',
	'TrailSurface': 'Surface_Type',
	'Name_OfficialSummer_Primary': 'Trail_Name',
    'Shape_Length': 'Length_m',
    'Summer_Type': 'Summer_Use',
    'Winter_Type': 'Winter_Use'
})



df.to_csv('../data/interim/1_cleaned.csv', index=False)
