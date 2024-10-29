# .xls 파일 읽기
xls_file = excel_file_path
workbook_xls = xlrd.open_workbook(xls_file)
sheet_xls = workbook_xls.sheet_by_index(0)

# .xlsx 파일 생성
xlsx_file = excelx_file_path
workbook_xlsx = openpyxl.Workbook()
sheet_xlsx = workbook_xlsx.active

# .xls 데이터 복사하기
for row in range(sheet_xls.nrows):
    for col in range(sheet_xls.ncols):
        sheet_xlsx.cell(row=row + 1, column=col + 1).value = sheet_xls.cell_value(row, col)

# .xlsx 파일 저장
workbook_xlsx.save(xlsx_file)