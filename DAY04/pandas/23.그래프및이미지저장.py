import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터프레임 생성
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Sales': [150, 200, 300, 250, 400]
}

df = pd.DataFrame(data)

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b', label='Sales')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()

# 그래프를 이미지 파일로 저장
plt.savefig('monthly_sales.png')

# 그래프 보여주기
plt.show()