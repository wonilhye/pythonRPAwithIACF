import util #util 클래스 불러오기(프로그램 구현에 필요한 함수들을 만들어 놓은 집합체: cf. 패키지>클래스>함수)
import pandas as pd #pandas 패키지 불러와서 pd라고 별명짓기

# 현재 파이썬 파일의 디렉터리 위치 얻기
directory = util.crdir("py", False) #crdir → current directory의 줄임말

# 변형/가공할 엑셀(raw data) 파일 불러오기: 변수로 선언
excel_file_path = f"{directory}\\workF\\20241016_89900100056880_154004.xls" #f-string 활용

# 1. 불러온 엑셀 파일의 데이터를 읽어와서 헤더가 없으므로 pandas 컬럼인덱스를 임의로 지정하는 것 
df = pd.read_excel(excel_file_path, header=None)

# 2. 읽어온 엑셀 데이터의 키값(여기선 계좌번호) 중, 숫자만 추출하고 그것을 이름으로 하는 엑셀 파일 저장경로 설정
account_num = util.acctonum(df.iloc[0,0], "Bank")
output_file_path = f"{directory}\\resultF\\"+account_num+".xlsx" #결과 파일 경로 설정

# 3. 읽어온 엑셀 데이터의 1~6행을 삭제 후 지정경로에 엑셀 파일로 저장
df = df.drop(df.index[0:6])
df.to_excel(output_file_path, index=False, header=False)

# 4. 저장한 엑셀 파일의 데이터를 다시 읽어오기
df = pd.read_excel(output_file_path)

# 5. 읽어온 데이터 중, '거래일시' 값의 형태를 변형하고 정렬하기
df['거래일시'] = df['거래일시'].str.replace('.','', regex=False).str.slice(0, 8)
df = df.sort_values(by='거래일시')

# 6. 읽어온 데이터 중, 불필요한 열 삭제
df = df.drop(columns=['잔액(원)','내 통장 표시','적요','처리점','구분'])

# 7. 최종본을 지정경로에 엑셀 파일로 다시 저장
df.to_excel(output_file_path, index=False) #위에서 header 날렸기에 여기선 날리지 않음
