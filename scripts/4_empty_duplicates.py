import pandas as pd

df = pd.read_csv('../data/interim/3_cleaned.csv')

# Fill empty values with appropriate nulls for each dtype
for col in df.columns:
    from pandas.api.types import CategoricalDtype
    if isinstance(df[col].dtype, CategoricalDtype):
        df[col] = df[col].cat.add_categories(['']).fillna('')
    elif pd.api.types.is_bool_dtype(df[col]):
        df[col] = df[col].fillna(False)
    elif pd.api.types.is_float_dtype(df[col]):
        df[col] = df[col].fillna(float('nan'))
    elif pd.api.types.is_string_dtype(df[col]):
        df[col] = df[col].fillna('')
    else:
        df[col] = df[col].fillna('')

# Remove duplicate rows

df = df.drop_duplicates()

df.to_csv('../data/interim/4_cleaned.csv', index=False)
