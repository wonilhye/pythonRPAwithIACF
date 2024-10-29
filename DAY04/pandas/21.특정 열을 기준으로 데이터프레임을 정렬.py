import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df_sorted = df.sort_values('Age')
print(df_sorted)