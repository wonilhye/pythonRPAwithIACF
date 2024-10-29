import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df1 = pd.read_excel('data1.xlsx')
df2 = pd.read_excel('data2.xlsx')
merged = pd.merge(df1, df2, on='EmployeeID')
merged.to_excel('merged_data.xlsx', index=False)