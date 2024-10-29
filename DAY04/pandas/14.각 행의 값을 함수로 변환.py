import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df['Age'] = df['Age'].apply(lambda x: x + 1)
df.to_excel('age_incremented.xlsx', index=False)

#Age 열의 모든 값을 1씩 증가시키고, 결과를 age_incremented.xlsx에 저장
