import pandas as pd

df = pd.read_csv('../data/interim/5_cleaned.csv')

# Filter rows where population is missing
missing_pop = df[df['city_population'].isna()]

# Get unique city names
missing_cities = missing_pop['City'].unique()

print("Cities without population data:")
print(missing_cities)
