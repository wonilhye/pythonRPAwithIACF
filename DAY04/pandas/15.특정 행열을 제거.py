import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df_dropped = df.drop('Address', axis=1)
df_dropped.to_excel('data_without_address.xlsx', index=False)

# 특정 행 범위(5번째 행부터 10번째 행까지) 삭제
df_dropped = df.drop(df.index[5:10])