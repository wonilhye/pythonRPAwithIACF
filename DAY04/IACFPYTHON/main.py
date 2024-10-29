import util
import pandas as pd

# 현재 파일의 위치 얻기
directory = util.crdir("py", False)

# 설정 부분: 엑셀 파일 읽기
excel_file_path = f"{directory}\\workF\\20241016_89900100056880_154004.xls"  # 엑셀 파일 경로 설정

# 1. 엑셀 데이터 읽기
df = pd.read_excel(excel_file_path, header=None)

# 2. A1 셀의 계좌정보 가져와서 결과파일로 저장하기
account_num = util.acctonum(df.iloc[0, 0], "Bank")
output_file_path = f"{directory}\\resultF\\"+account_num+".xlsx"  # 결과 파일 경로 설정

# 3. 1~6행을 삭제한다.
df = df.drop(df.index[0:6])

df.to_excel(output_file_path, index=False, header=False)

df = pd.read_excel(output_file_path)


df['거래일시'] = df['거래일시'].str.replace('.', '', regex=False).str.slice(0, 8)
df = df.sort_values(by='거래일시')

df = df.drop(columns=['잔액(원)','내 통장 표시','적요','처리점','구분'])

# 99. 파일저장
df.to_excel(output_file_path, index=False)