import pandas as pd

df = pd.read_csv('../data/raw/minnesota-cities-by-population-2025.csv')

# Remove quotes from all string columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.replace('"', '', regex=False)

# Keep only 'city' and 'pop2024' columns
df = df[['city', 'pop2024']]

df.to_csv('../data/interim/minnesota-cities-pop2024-cleaned.csv', index=False)