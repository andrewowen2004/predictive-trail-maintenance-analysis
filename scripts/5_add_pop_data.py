import pandas as pd

# Read your main CSV and the population CSV
df_main = pd.read_csv('main.csv')
df_pop = pd.read_csv('population.csv')  # Should have columns: 'City', 'Population'

# Merge on the 'City' column
df_merged = df_main.merge(df_pop, on='City', how='left')

# Save the result
df_merged.to_csv('main_with_population.csv', index=False)

### Potential solution to add population data to the main dataset:
# 1. Read the main dataset and the population dataset.
# 2. Merge them on the 'City' column.
# 3. Save the merged dataset to a new CSV file. 