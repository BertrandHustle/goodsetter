import sys
import os

args = sys.argv

if len(args) != 2:
    print ("Usage: goodsetter <directory>")
else:
    directory_path = args[1]
    os.chdir(directory_path)
    directory = os.listdir(directory_path)
    for file in directory:
        file = ("\""+file+"\"")
        os.system('7z e ' + file)

        #add handling for .7z w/multiple files
