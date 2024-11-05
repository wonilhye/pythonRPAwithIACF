import re
import os
from openpyxl import load_workbook

def crdir(chk="dir" ,display=False) : 
    directory = ""
    if chk == "dir" : # 현재 디렉토리 위치 얻기
        directory = os.getcwd()
    elif chk == "py"  : # 현재 파이썬 파일 디렉토리 위치 얻기
        directory = os.path.dirname(os.path.abspath(__file__))
    else :
        directory = "dir or py를 선택하세요."
    if display == True :
        print("현재 디렉토리 : " + directory)
    return directory

def acctonum(account_number) :
    # 정규식 패턴
    pattern = r'(\d{6}-?\d{2}-?\d{6})|(\d{12,})'
    # 계좌번호 추출
    result = re.search(pattern, account_number)
    account_number = result.group().replace('-', '') if result else None
    return str(account_number)