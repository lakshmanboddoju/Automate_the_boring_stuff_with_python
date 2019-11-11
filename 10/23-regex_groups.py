#! python3

import re

message = 'My number is 415-555-4242 or (415) 555-4242'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search(message)
matchObject2 = phoneNumRegex2.search(message)

print(matchObject.group(1))
print(matchObject.group(2))

print(matchObject2.group())
print(matchObject2.group(1))
print(matchObject2.group(2))
