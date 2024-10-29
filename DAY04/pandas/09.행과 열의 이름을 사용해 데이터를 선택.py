import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

subset = df.loc[:, ['Name', 'Age']] # `df.loc[:, ['Name', 'Age']]`는 데이터프레임 `df`에서 모든 행의 `Name`과 `Age` 열을 선택하여 새로운 데이터프레임으로 반환하는 코드
subset.to_excel('subset.xlsx', index=False)

#첫 번째 행의 Name 열 값을 반환합니다.
row = df.loc[0, 'Name']
print(row)
