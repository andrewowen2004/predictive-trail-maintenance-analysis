import pandas as pd

df = pd.read_csv('../data/raw/raw_trail_data.csv')

df.drop(columns=['GlobalID','County','DataGrade','DataSource','created_date','last_edited_date','MapWebWinter','MapWebSummer','Name_OfficialWinter_Primary',], axis=1, inplace=True)

df.to_csv('../data/interim/0_cleaned.csv', index=False)

