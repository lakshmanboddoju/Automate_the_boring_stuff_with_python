#! python3

import docx

def getAllText(filename):
    doc = docx.Document(filename)
    allText = []
    for para in  doc.paragraphs:
        allText.append(para.text)
    return '\n'.join(allText)

print()
print(getAllText(r'D:\Users\pavan\Documents\GitHub-lakshmanboddoju\Automate_the_boring_stuff_with_python\14\demo.docx'))
