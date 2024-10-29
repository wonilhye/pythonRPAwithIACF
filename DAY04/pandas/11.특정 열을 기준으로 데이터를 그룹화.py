import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

grouped = df.groupby('Department').sum()
grouped.to_excel('grouped_data.xlsx')