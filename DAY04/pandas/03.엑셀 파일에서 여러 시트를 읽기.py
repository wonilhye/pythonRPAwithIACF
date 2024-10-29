import pandas as pd

df = pd.read_excel('data.xlsx')
print(df)

excel_file = pd.ExcelFile('data.xlsx')
print(excel_file.sheet_names)
