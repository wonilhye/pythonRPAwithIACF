#0_새로 만든 xlsxProcess 클래스를 불러와서 xlp로 명명하기
import xlsxProcess as xlp

#1_불러올 파일(raw data)의 이름을 변수에 저장하기
filename = "20241016_89900100056880_154004"
""" idea_1. input으로 특정 파일 선택하여 돌리기: filename=input("파일명을 입력하세요: ") → 근데 굳이?
    idea_2. for 반복문을 통해 폴더 내 파일명 주르륵 훑기 → 파일명이 규칙적인 수열 패턴일 때 가능할 듯
    idea_3. selectfolder와 같이 폴더 내 파일명을 리스트로 추출해서 for 반복문으로 주르륵 훑기"""

#2_xlp 클래스의 toExcelErp라는 함수를 실행하기
xlp.toExcelErp(filename)