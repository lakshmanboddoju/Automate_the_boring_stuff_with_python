#! python3

import os

for folderName, subFolders, fileNames in os.walk('C:\\Users\\pavan\\Desktop\\lakshman-website'):
    print('The folder is ' + folderName)
    print('The subFolders in ' + folderName + ' are: ' + str(subFolders))
    print('The fileNames in ' + folderName + ' are: ' + str(fileNames))
    print()

