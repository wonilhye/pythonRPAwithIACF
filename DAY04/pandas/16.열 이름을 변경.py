import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df_renamed = df.rename(columns={'Name': 'Full Name'})
df_renamed.to_excel('renamed_columns.xlsx', index=False)