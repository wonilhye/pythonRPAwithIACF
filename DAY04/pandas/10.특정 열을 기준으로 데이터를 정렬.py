import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df_sorted = df.sort_values('Age')
df_sorted.to_excel('sorted_data.xlsx', index=False)