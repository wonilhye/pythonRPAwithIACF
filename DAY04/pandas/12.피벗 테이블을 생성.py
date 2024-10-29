import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

pivot = df.pivot_table(index='Department', columns='Gender', values='Salary', aggfunc='mean')
pivot.to_excel('pivot_table.xlsx')
