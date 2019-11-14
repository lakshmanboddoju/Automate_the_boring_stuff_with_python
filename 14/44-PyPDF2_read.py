#! python3

import os, PyPDF2

os.chdir('D:\\Users\\pavan\\Documents\\GitHub-lakshmanboddoju\\Automate_the_boring_stuff_with_python\\14')

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

pageObj = reader.getPage(0)
print(pageObj.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

