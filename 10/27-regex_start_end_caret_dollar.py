#! python3

import re

beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello there!')
mo2 = beginsWithHelloRegex.search('ya Hello')

print(mo.group())
try:
    print(mo2.group())
except:
    print('Didnt match: ' + str(beginsWithHelloRegex))

endsWithWorldRegex = re.compile(r'world!$')
mo3 = endsWithWorldRegex.search('Hello world!')
mo4 = endsWithWorldRegex.search('world lalala.')

print(mo3.group())
try:
    print(mo4.group())
except:
    print('Didnt match: ' + str(endsWithWorldRegex))

allDigitsRegex = re.compile(r'^\d+$')

mo5 = allDigitsRegex.search('12322132334577')
mo6 = allDigitsRegex.search('171727272x73732')

print(mo5.group())

try:
    print(mo6.group())
except:
    print('Didnt match: ' + str(allDigitsRegex))

#. matches any single character but a new line.
atRegex = re.compile(r'.at')
mo7 = atRegex.findall('The cat in the hat sat on the flat mat.')

print(mo7)

atRegex2 = re.compile(r'.{1,2}at')
mo8 = atRegex2.findall('The cat in the hat sat on the flat mat.')

print(mo8)


nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
textStr = 'First Name: Lakshman Last Name: Boddoju'
mo9 = nameRegex.findall(textStr)

print(mo9)

# .*? is non greedy
serve = '<To serve humans> for dinner.>'
nonGreedyRegex = re.compile(r'<(.*?)>')
print(nonGreedyRegex.findall(serve))

# .* is greedy
greedyRegex = re.compile(r'<(.*)>')
print(greedyRegex.findall(serve))


prime = 'Serve the public trust. \nProtect the innocent. \nUphold the law.'
dotStar = re.compile(r'.*')
print(dotStar.search(prime).group())

# to include even new lines
dotStarAll = re.compile(r'.*', re.DOTALL)
print(dotStarAll.search(prime).group())

vowelRegexAgain = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowelRegexAgain.findall('Al, why does your programming book talk about RoboCop so much?'))
