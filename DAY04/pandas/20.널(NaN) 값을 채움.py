import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df_filled = df.fillna(0)
print(df_filled)