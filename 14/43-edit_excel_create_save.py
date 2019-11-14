import os, openpyxl

os.chdir(r'D:\Users\pavan\Documents\GitHub-lakshmanboddoju\Automate_the_boring_stuff_with_python\14')

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')

sheet['A1'] = 42
sheet['A2'] = 'Hello World!'

wb.save('exampleSaved.xlsx')
