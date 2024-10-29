import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

# iloc : 인덱스 기반 => 2번째 행(Charlie)와 1번째 열(Age) 값을 가져옴
value = df.iloc[2, 1]
print(value)  # 출력: 45

# at[]는 라벨 기반 => 행 라벨 3(David), 열 라벨 'aaa' 값을 가져옴
value = df.at[3, 'aaa']
print(value)  # 출력: Houston