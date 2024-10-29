import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df_clean = df.dropna()
df_clean.to_excel('clean_data.xlsx', index=False)
