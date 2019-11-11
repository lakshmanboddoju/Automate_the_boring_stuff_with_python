#! python3

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex.findall('You can reach me at 123-222-3333 or 122-333-4444'))

phoneRegex2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex2.findall('You can reach me at 123-222-3333 or 122-333-4444'))


lyrics = 'On the 12th day of Christmas my true love sent to me 12 drummers drumming, 11 pipers piping, 10 lords a-leaping, Nine ladies dancing, Eight maids a-milking, Seven swans a-swimming, Six geese a-laying, Five golden rings, Four calling birds, Three french hens, Two turtle doves, and A partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))

vowelRegex = re.compile(r'[aeiouAEIOU]{2}')
nonVowelRegex = re.compile(r'[^aeiouAEIOU]')
testString = 'Robocop eats baby food.'
print(vowelRegex.findall(testString))
print(nonVowelRegex.findall(testString))
