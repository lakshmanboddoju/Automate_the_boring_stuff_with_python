#! python3

import shelve

# Read Operation

helloFile = open('C:\\Users\\lakshman\\Desktop\\hello.txt')
#helloFileContent = helloFile.read()
#print(helloFileContent)
print(helloFile.readlines())
helloFile.close()


# Write Operation

helloFile2 = open('C:\\Users\\lakshman\\Desktop\\hello2.txt', 'w')
helloFile2.write('YOLO!\n')
helloFile2.write('You Rock!\n')
helloFile2.close()


# Append Operation

helloFile3 = open('C:\\Users\\lakshman\\Desktop\\hello3.txt', 'a')
helloFile3.write('YOLO!\n')
helloFile3.write('You Rock!\n')
helloFile3.close()


# Shelve File | Persistent memory for complex stuff to store like lists, etc.

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()
