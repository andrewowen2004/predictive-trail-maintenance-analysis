import pandas as pd

# Read cleaned trail data and city population data
trail_df = pd.read_csv('../data/interim/4_cleaned.csv')
pop_df = pd.read_csv('../data/interim/minnesota-cities-pop2024-cleaned.csv')

# Rename pop_df column so it matches trail_df's 'City'
pop_df = pop_df.rename(columns={'city': 'City'})

# Merge population data into trail data by City
merged_df = trail_df.merge(pop_df, on='City', how='left')

# Rename the population column
merged_df = merged_df.rename(columns={'pop2024': 'city_population'})

# Save the result
merged_df.to_csv('../data/interim/5_cleaned.csv', index=False)


