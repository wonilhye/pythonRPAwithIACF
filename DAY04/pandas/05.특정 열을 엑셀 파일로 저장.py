import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df['Age'].to_excel('age_data.xlsx', index=False)