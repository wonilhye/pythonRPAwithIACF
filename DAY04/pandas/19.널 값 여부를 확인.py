import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

null_values = df.isnull()
print(null_values)

#널 값이 있는지 확인하여 불리언 값(True/False)으로 나타냄