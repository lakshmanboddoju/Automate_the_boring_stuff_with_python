#! python3

import os, openpyxl

os.chdir(r'D:\Users\pavan\Documents\GitHub-lakshmanboddoju\Automate_the_boring_stuff_with_python\14')

wb = openpyxl.load_workbook('exampleSaved.xlsx')
print(str(wb.get_sheet_by_name('Sheet')['A1'].value))
sheet2 = wb.create_sheet()
sheet2.title = 'MyNewSheet'
wb.save('example2.xlsx')

wb = openpyxl.load_workbook('exampleSaved.xlsx')
wb.create_sheet(title = 'MyOtherSheet', index = 0)
wb.save('example2.xlsx')
