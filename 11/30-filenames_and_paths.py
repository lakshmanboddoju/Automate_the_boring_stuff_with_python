#! python3

import os

totalSize = 0

for filename in os.listdir(r'C:\Users\lakshman\Desktop'):
    if os.path.isfile(os.path.join('C:\\Users\\lakshman\\Desktop\\', filename)):
        continue
    else:
        totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\lakshman\\Desktop\\', filename))

print(totalSize)
