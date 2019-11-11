#! python3

import re

# ? groups ==> can appear zero or one times.

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman.')

try:
    print(mo.group())
except:
    print('Doesnt match regex: ' + str(batRegex))


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo2 = phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')

print(mo2.group())

batRegex2 = re.compile(r'Bat(wo)*man')
mo3 = batRegex2.search('The adventures of Batwowowoman.')

print(mo3.group())

batRegex3 = re.compile(r'Bat(wo)+man')
mo4 = batRegex3.search('The adventures of Batman.')

try:
    print(mo4.group())
except:
    print('Doesnt match regex: ' + str(batRegex3))

mo4 = batRegex3.search('The adventures of Batwowoman.')
print(mo4.group())


regex = re.compile(r'\+\*\?')
mo5 = regex.search('I learned about +*? regex syntax')
print(mo5.group())

ha3TimesRegex = re.compile(r'(Ha){3}')
mo6 = ha3TimesRegex.search('HaHaHa')
print(mo6.group())

phoneRegex2 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?( )?){3}')
mo7 = phoneRegex2.search('My numbers are 415-555-1234,555-4242, 213-555-0000')
print(mo7.group())

haMinMaxRegex = re.compile(r'(Ha){3,5}')
mo8 = haMinMaxRegex.search('MuHaHaHaHa')
print(mo8.group())

#Greedy Match
digitRegex = re.compile(r'(\d){3,5}')
mo9 = digitRegex.search('1234567890')
print(mo9.group())

#Non Greedy Match
digitRegex2 = re.compile(r'(\d){3,5}?')
mo10 = digitRegex2.search('1234567890')
print(mo10.group())
