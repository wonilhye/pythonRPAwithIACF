import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df.to_excel('output.xlsx', sheet_name='MySheet', index=False)

