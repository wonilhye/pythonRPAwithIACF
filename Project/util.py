import re
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
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

def select_folder(display=False):
    """
    사용자가 폴더를 선택할 수 있게 하고, 선택된 폴더의 파일 목록을 반환합니다.
    """
    # Tkinter 창을 숨기기
    root = tk.Tk()
    root.withdraw()
    
    # 폴더 선택 대화상자 열기
    folder_path = filedialog.askdirectory(title="폴더를 선택하세요")
    
    # 선택된 폴더가 없으면 종료
    if not folder_path:
        print("폴더가 선택되지 않았습니다.")
        return None

    # 폴더의 파일 목록 가져오기
    file_list = os.listdir(folder_path)
    if display : print(f"선택된 폴더: {folder_path}")
    
    # 특정 확장자 필터링 (.csv, .xlsx 파일만 가져오기)
    data_files = [file for file in file_list if file.endswith('.csv') or file.endswith('.xlsx') or file.endswith('.xls')]
    if display : print("데이터 파일 목록:", data_files)
    
    # 파일 경로와 이름을 포함한 DataFrame 생성 (선택 사항)
    df_files = pd.DataFrame({
        'file_name': data_files,
        'file_path': [os.path.join(folder_path, file) for file in data_files]
    })
    
    return df_files
