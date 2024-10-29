import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

selected_data = df.iloc[0:5, 1:3]
selected_data.to_excel('selected_data.xlsx', index=False)