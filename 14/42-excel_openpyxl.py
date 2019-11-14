import os, openpyxl

os.chdir(r'D:\Users\pavan\Documents\GitHub-lakshmanboddoju\Automate_the_boring_stuff_with_python\14')

workbook = openpyxl.load_workbook('example.xlsx')
workbook.get_sheet_names()
sheet = workbook.get_sheet_by_name('Sheet1')
cell = sheet['B1']

print(str(cell.value))

print(str(sheet.cell(row = 2, column = 2)))

for i in range(1, 8):
	  print(i, str(sheet.cell(row = i, columnn = 2).value))
