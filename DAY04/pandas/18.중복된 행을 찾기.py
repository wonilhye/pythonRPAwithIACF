import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

duplicates = df[df.duplicated()]
duplicates.to_excel('duplicates.xlsx', index=False)

#중복된 행만 선택해 duplicates.xlsx로 저장