import util
import pandas as pd

df_bank_name = "은행자료"
df_saer_name = "회계자료"
df_comb_name = "시트합치기"
df_pivO_name = "피봇출금"
df_pivI_name = "피봇입금"

def toExcelErp(filename) :
    # 1. 현재 파일의 위치 얻기
    directory = util.crdir("py", False)

    # 2. 파일 위치 알기    
    filename2 = filename.split('_')[1][-6:]
    account_num = filename.split('_')[1]
    excel_file_path_bank = f"{directory}\\workF\\{filename}.xls"
    excel_file_path_saer = f"{directory}\\workF\\거래처원장 {filename2}.xls"

    df_bank = pd.read_excel(excel_file_path_bank, header=None)
    df_saer = pd.read_excel(excel_file_path_saer, header=None)

    # 3. 결과 파일
    output_file_path = f"{directory}\\resultF\\"+account_num+".xlsx"  # 결과 파일 경로 설정

    # 4. 행을 삭제한다
    df_bank = df_bank.drop(df_bank.index[0:6])
    df_saer = df_saer.drop(df_saer.index[0:7])

    # 5. 파일 1차 저장
    with pd.ExcelWriter(output_file_path) as writer:
        df_bank.to_excel(writer, sheet_name=df_bank_name, index=False, header=False)
        df_saer.to_excel(writer, sheet_name=df_saer_name, index=False, header=False)

    # 6. 특정 시트 읽기
    df_bank = pd.read_excel(output_file_path, sheet_name=df_bank_name)
    df_saer = pd.read_excel(output_file_path, sheet_name=df_saer_name)

    # 7. 시트별 비즈니즈 로직
    # df_bank 로직
    df_bank['거래일시'] = df_bank['거래일시'].str.replace('.', '', regex=False).str.slice(0, 8)
    df_bank = df_bank.sort_values(by='거래일시')
    df_bank = df_bank.drop(columns=['잔액(원)','내 통장 표시','적요','처리점','구분'])
    # df_saer 로직
    df_saer['일자'] = df_saer['일자'].str.replace('-', '', regex=False).str.slice(0, 8)
    df_saer = df_saer.sort_values(by='일자')
    df_saer = df_saer[~df_saer['일자'].str.contains('전기 이월|월계|누계', na=False)]
    df_saer = df_saer[~df_saer['적요'].str.contains('합계', na=False)]
    df_saer = df_saer.drop(columns=['전표번호','계정명','잔액','회계단위명'])

    # 7. 시트 합치기
    df_bank = df_bank[['거래일시', '출금액(원)','입금액(원)']]
    df_bank.columns = ['거래일시','출금','입급']
    df_bank.insert(0, '구분', df_bank_name)  # 신규 구분 컬럼을 첫 번째 위치에 추가

    df_saer = df_saer[['일자', '대변','차변']]
    df_saer.columns = ['거래일시','출금','입급']
    df_saer.insert(0, '구분', df_saer_name)  # 신규 구분 컬럼을 첫 번째 위치에 추가

    df_comb = pd.concat([df_bank, df_saer], ignore_index=True)

    # 8. 피봇 만들기
    # 8-1. 출금 피벗 테이블 생성
    df_pivO = df_comb.pivot_table(
        index='거래일시', columns='구분', values='출금', aggfunc='sum', fill_value=0)
    df_pivO['출금차액'] = df_pivO.get(df_bank_name, 0) - df_pivO.get(df_saer_name, 0)
    df_pivO['상태'] = df_pivO['출금차액'].apply(lambda x: '정상' if x == 0 else '오류')
    # 8-2. 입금 피벗 테이블 생성
    df_pivI = df_comb.pivot_table(
        index='거래일시', columns='구분', values='출금', aggfunc='sum', fill_value=0)
    df_pivI['출금차액'] = df_pivI[df_bank_name] - df_pivI.get(df_saer_name, 0)
    df_pivI['상태'] = df_pivI['출금차액'].apply(lambda x: '정상' if x == 0 else '오류')

    # 9. 파일 최종 저장
    with pd.ExcelWriter(output_file_path) as writer:
        df_bank.to_excel(writer, sheet_name=df_bank_name, index=False)
        df_saer.to_excel(writer, sheet_name=df_saer_name, index=False)
        df_comb.to_excel(writer, sheet_name=df_comb_name, index=False)
        df_pivO.to_excel(writer, sheet_name=df_pivO_name)
        df_pivI.to_excel(writer, sheet_name=df_pivI_name)
