#! python3

import re, pyperclip


# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# Types of phone numbers to match
# 415-555-0000
# 555-0000
# (415) 555-0000
# 555-0000 ext 12345
# 555-0000 ext. 12345
# 415-555-0000 x12345

# area code (optional)
(
((\d\d\d)|(\(\d\d\d\)))?

# first seperator
(\s|-)

# first 3 digits
\d\d\d

# seperator
-

# last 4 digits
\d\d\d\d

# extension (optional)
((ext(\.)?\s)|x         # word part
 (\d{2,5}))?            # 2-5 number extension
)

''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# Types of email addresses to match
# some.+_thing@something.com

# name
[a-zA-Z0-9_.+]+

# @ symbol
@

# domain name
[a-zA-Z0-9_.+]+

''', re.VERBOSE)
# Get text from clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhoneList = phoneRegex.findall(text)
extractedEmailList = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNumber in extractedPhoneList:
    allPhoneNumbers.append(phoneNumber[0])
    
#print(allPhoneNumbers)
#print(extractedEmailList)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmailList)

pyperclip.copy(results)
