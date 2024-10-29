import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

df.insert(2, 'Age Group', ['Adult', 'Senior', 'Child', 'Teenager', 'Adult'])
df.to_excel('data_with_age_group.xlsx', index=False)

#Age Group이라는 새로운 열을 세 번째 위치에 추가하고, 결과를 data_with_age_group.xlsx에 저장