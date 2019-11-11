#! python3

import re

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

namesRegex2 = re.compile(r'Agent (\w)\w*')
print(namesRegex2.findall('Agent Alice gave the secret documents to Agent Bob.'))

#the \1 prints the first group in the regex and can be used to print certain portions of the original string
print(namesRegex2.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))


# VERBOSE helps us add spaces and comments inside the multiline string for readability
phoneRegex = re.compile(r'''
\(\d\d\d)                   # area code
(-)?                        # first dash optional
\d\d\d                      # next 3 digits
-                           # second dash 
\d\d\d\d''', re.VERBOSE)    # last 4 digits
