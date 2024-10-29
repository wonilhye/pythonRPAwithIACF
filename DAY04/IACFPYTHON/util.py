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

def acctonum(account_number, chk="Bank") :
    numbers_only = 0
    numbers_string = ""
    if chk == "Bank" :
        # 정규식 패턴 사용하여 숫자만 추출
        numbers_only = re.findall(r'\d+', account_number)
    else :
        # 정규식 패턴 사용하여 숫자만 추출
        numbers_only = re.findall(r'\d{11,16}', account_number)
    # 리스트를 하나의 문자열로 합치기
    numbers_string = ''.join(numbers_only)
    return str(numbers_string)

def autowidth(output_file_path) :
    # 엑셀 파일 불러오기
    workbook = load_workbook(output_file_path)
    sheet = workbook.active

    # 각 열의 너비 자동 조정
    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter  # 열 레터 (A, B, C 등)
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)  # 여유 공간 추가
        sheet.column_dimensions[column_letter].width = adjusted_width

    # 수정된 엑셀 파일 저장
    workbook.save(output_file_path)