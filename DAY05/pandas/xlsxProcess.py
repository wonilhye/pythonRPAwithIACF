#0_util 클래스 불러오기: cf. util은 주임님이 만드신 함수들의 집합체(=클래스)임
import util
#1_pandas 클래스 불러와서 pd로 명명하기
import pandas as pd

#2_새로 정의할 함수("toExcelErp") 안에서 사용하는 변수 설정하기: 여기선 출력물(엑셀파일)의 시트명
df_bank_name = "은행자료"
df_saer_name = "회계자료"
df_comb_name = "시트합치기"
df_pivO_name = "피봇출금"
df_pivI_name = "피봇입금"

#3_새로운 함수 정의하기
def toExcelErp(filename) :
    # 0) 현재 파일의 위치 얻기
    directory = util.crdir("py", False)

    # 1) raw data 파일명에서 계좌번호만 추출해서 사용하기
    #    1-1) filename에서 underbar(_) 기점으로 데이터 분리 후 리스트 생성: .split('_')
    #         → 리스트의 1번째 값을 가져오기: .split('_')[1]
    #         → 가져온 값의 뒤(오른쪽)에서부터 6자리까지만 변수 값으로 설정하기: .split('_')[1][-6:]
    filename2 = filename.split('_')[1][-6:]
    #    1-2) 위에서 만든 filename2 리스트 값 중 1번째 값이 계좌번호이므로 이를 변수의 값으로 설정하기
    account_num = filename.split('_')[1]
    
    # 2) 작업이 필요한 raw data 의 위치값을 불러와서 각 변수에 저장하기
    excel_file_path_bank = f"{directory}\\workF\\{filename}.xls"
    excel_file_path_saer = f"{directory}\\workF\\거래처원장 {filename2}.xls"

    # 3) 위에서 지정한 디렉터리에 있는 엑셀 파일을 불러와서 데이터프레임(엑셀표)을 각 변수에 저장하기
    #    ※1_raw data 파일이 2개니까 각각의 데이터 프레임을 각 변수에 저장함: df_bank, df_saer(sanerp줄임말)
    #    ※2_실습 파일은 header가 없으므로 pandas 컬럼 인덱스를 임의 지정
    df_bank = pd.read_excel(excel_file_path_bank, header=None)
    df_saer = pd.read_excel(excel_file_path_saer, header=None)

    # 4) 작업 후 생성되는 파일을 저장할 위치를 지정하고 위치값을 변수에 저장하기(여기서 파일명은 계좌번호)
    output_file_path = f"{directory}\\resultF\\"+account_num+".xlsx"

    # 5) '#3)'에서 불러온 데이터프레임(엑셀표)에서 불필요한 행을 제거하기
    df_bank = df_bank.drop(df_bank.index[0:6]) #1~6행 제거
    df_saer = df_saer.drop(df_saer.index[0:7]) #1~7행 제거

    # 6) 파일 1차 저장
    #    → '#3)'에서 불러오고, '#5)'에서 가공한 데이터프레임을, '#4)'에서 저장한 위치에 엑셀파일 형태로 저장하기
    with pd.ExcelWriter(output_file_path) as writer:
        df_bank.to_excel(writer, sheet_name=df_bank_name, index=False, header=False) #sheet 이름을 지정 후 저장
        df_saer.to_excel(writer, sheet_name=df_saer_name, index=False, header=False) #another sheet 이름을 지정 후 저장

    # 7) 위에서 저장한 엑셀파일의 각 시트를 불러와서 데이터프레임(엑셀표)을 각 변수에 저장하기
    df_bank = pd.read_excel(output_file_path, sheet_name=df_bank_name)
    df_saer = pd.read_excel(output_file_path, sheet_name=df_saer_name)

    # 8) 불러온 각 시트별 데이터 가공하기
    #    8-1) df_bank 변수에 저장한 데이터의 가공
    df_bank['거래일시'] = df_bank['거래일시'].str.replace('.', '', regex=False).str.slice(0, 8) #거래일시값 가공
    df_bank = df_bank.sort_values(by='거래일시') #거래일시 기준으로 정렬
    df_bank = df_bank.drop(columns=['잔액(원)','내 통장 표시','적요','처리점','구분']) #불필요한 열 삭제
    #    8-2) df_saer 변수에 저장한 데이터의 가공
    df_saer['일자'] = df_saer['일자'].str.replace('-', '', regex=False).str.slice(0, 8) #일자값 가공
    df_saer = df_saer.sort_values(by='일자') #일자 기준으로 정렬
    df_saer = df_saer[~df_saer['일자'].str.contains('전기 이월|월계|누계', na=False)] #'일자'열에서 특정 단어 포함한 행 삭제
    df_saer = df_saer[~df_saer['적요'].str.contains('합계', na=False)] #'적요'열에서 특정 단어 포함한 행 삭제
    df_saer = df_saer.drop(columns=['전표번호','계정명','잔액','회계단위명']) #불필요한 열 삭제

    # 9) 비교를 위해 가공한 각 시트를 하나의 시트로 합치기
    #    9-1) df_bank_name 시트의 데이터프레임 가공하기
    df_bank = df_bank[['거래일시', '출금액(원)','입금액(원)']] #df_bank_name 시트에서 값을 비교할 컬럼 선택
    df_bank.columns = ['거래일시','출금','입금'] #비교 가능하도록 공통된 기준으로 컬럼명 변경
    df_bank.insert(0, '구분', df_bank_name)  #0번째 위치에 신규 컬럼을 추가하기: 컬럼명은 "구분"
    #    9-2) df_saer_name 시트의 데이터프레임 가공하기
    df_saer = df_saer[['일자', '대변','차변']] #df_saer_name 시트에서 값을 비교할 컬럼 선택
    df_saer.columns = ['거래일시','출금','입금'] #비교 가능하도록 공통된 기준으로 컬럼명 변경
    df_saer.insert(0, '구분', df_saer_name)  #0번째 위치에 신규 컬럼을 추가하기: 컬럼명은 "구분"
    #    9-3) 가공한 두 시트를 합쳐서 다른 시트에 저장하기 위해 새로운 변수를 선언하고 데이터프레임(엑셀표) 저장하기
    df_comb = pd.concat([df_bank, df_saer], ignore_index=True)

    # 10) 피봇 만들기
    #    10-1) 출금 피벗 테이블 생성
    df_pivO = df_comb.pivot_table(
        index='거래일시', columns='구분', values='출금', aggfunc='sum', fill_value=0)
    #          ※1_두 시트 간 차액을 계산하여 "출금차액"이라는 새로운 컬럼에 표기하기
    df_pivO['출금차액'] = df_pivO.get(df_bank_name, 0) - df_pivO.get(df_saer_name, 0)
    #          ※2_계산한 "출금차액"이 0이 아닌 경우 "상태"라는 새로운 컬럼에 "오류"표기
    df_pivO['상태'] = df_pivO['출금차액'].apply(lambda x: '정상' if x == 0 else '오류')
    #    10-2) 입금 피벗 테이블 생성
    df_pivI = df_comb.pivot_table(
        index='거래일시', columns='구분', values='출금', aggfunc='sum', fill_value=0)
    #          ※1_두 시트 간 차액을 계산하여 "출금차액"이라는 새로운 컬럼에 표기하기
    df_pivI['출금차액'] = df_pivI[df_bank_name] - df_pivI.get(df_saer_name, 0)
    #          ※2_계산한 "출금차액"이 0이 아닌 경우 "상태"라는 새로운 컬럼에 "오류"표기
    df_pivI['상태'] = df_pivI['출금차액'].apply(lambda x: '정상' if x == 0 else '오류')

    # 11) 파일 최종 저장
    with pd.ExcelWriter(output_file_path) as writer:
        df_bank.to_excel(writer, sheet_name=df_bank_name, index=False)
        df_saer.to_excel(writer, sheet_name=df_saer_name, index=False)
        df_comb.to_excel(writer, sheet_name=df_comb_name, index=False)
        df_pivO.to_excel(writer, sheet_name=df_pivO_name)
        df_pivI.to_excel(writer, sheet_name=df_pivI_name)
