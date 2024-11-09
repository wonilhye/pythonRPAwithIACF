### 1. config.txt
 - ID, PW가 담긴 설정파일
 - main.py와 같은 위치에 있어야 함
 - 파일 내용 : ID, PW 한줄씩
 
### 2. workers.xlsx
 - "계좌번호, 성명, 메일"이 담긴 파일
 
계좌번호  | 성명 | 메일
------------- | ------------- | -------------
888888888  | 홍길동 | honggildong@abc.co.kr
888888889  | 홍길순 | honggilsoon@abc.co.kr

### 3. main.py
1. 모듈
   - 사용자 모듈 : util, xlsxProcess, webProcess
   - 시스템 모듈 : sys, os
2. 변수
   - log_display = False
3. 로직
   - 1.설정 파일의 내용을 읽어 값을 가져옴
     - get_iogin_info() 
   - 2.작업폴더를 선택하고 메일에서 파일을 가저옴
     - 사용자 다운로드 기본폴더 : os.path.expandvars(r"%UserProfile%\\Downloads"
     - 파일 다운로드 폴더 : Downloads\\workF
     - 엑셀처리 결과 폴더 : Downloads\\resultF
   - 3.엑셀 파일 처리 - 피봇
     - 작업폴더 읽기 : os.listdir(folder_workF_path)
     - toExcelErp(folder_workF_path, file_name)를 loop문으로 체크
   - 4.resulrF에 있는 오류결과 파일을 담당자에게 전송한다.
     - wep.login_drvier(logininfo)로 브라우저에서 로그인
     - 4.1 담당자엑셀을 읽어서 메일을 보낼 주소를 가져온다.
          - xlp.get_worker(folder_path, file_name)에서 사용자정보를 가져온다 
     - 4.2 담당자에게 해당 오류 파일을 전송한다.
          - send_mail_item을 만든다.
              - 받는사람(to_user), 제목(subject), 첨부파일(attach_file), 내용(contents)
   - 5.프로그램 종료 

### 4. xlsxProcess.py (xlp)
1. 모듈
   - 사용자 모듈 : util
   - 시스템 모듈 : pandas
2. 변수
   - log_display = False
3. 로직
  - SHEET_NAMES을 지정한다.
     - 계좌 번호 추출 및 파일 경로 설정
     - 초기 저장 (은행 자료, 회계 자료)
     - 특정 시트를 읽어서 비즈니스 로직 처리
        - 데이터 가공 및 정리
            - preprocess_bank_data(), preprocess_saer_data()
        - 시트 합치기
            - combine_df_data() 
     - 피봇 테이블 생성
        - create_pivot_tables()
     - 최종 저장 
### 5. webProcess.py (wep)
1. 모듈
   - 사용자 모듈 : util
   - 시스템 모듈 : time, selenium
2. 변수
   - log_display = False
3. 로직
   - 파일 다운로드
     - get_attach_file()
   - 파일 첨부하기
     - set_attach_file()
   - 로그인
     - login_drvier()
### 6. util.py (ut)
1. 모듈
   - 사용자 모듈 : -
   - 시스템 모듈 : re, os, inspect, logging, datetime, tkinter, openpyxl, PyQt5
2. 변수
   - log_display = False
   - today = datetime.datetime.now().strftime("%Y%m%d")  # 'YYYYMMDD' 형식
   - log_filename = os.path.expandvars(r"%UserProfile%\\Downloads\\log_" + today + ".txt")
3. 로직
   - 로그 설정 (파일 저장)
     - logging.basicConfig()
   - 디렉토리 위치 얻기
     - crdir()
   - 계좌번호 정규식 추출
     - acctonum()
   - 폴더 위치 지정
     - select_folder()
   - 폴더 생성
     - create_folder()
   - 이름이 같은 파일이 있으면 연번으로 파일 이름 생성하기
     - save_excel_with_seq()
   - 설정(config.txt) 파일을 읽어서 정보 얻기
     - main.py와 같은 위치
     - get_login_info()
   - 로그 찍기
     - print를 대체하기 위한 함수
     - logging.basicConfig()와 연관되어 있음
     - debug_print()
