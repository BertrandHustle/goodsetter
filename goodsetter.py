import sys
import os
import re

args = sys.argv

if len(args) != 2:
    print ('Usage: goodsetter <directory>'')
else:
    directory_path = args[1]
    os.chdir(directory_path)
    directory = os.listdir(directory_path)
    # unzip all the zip files
    for file in directory:
        file = ('\''+file+'\'')
        os.system('7z e ' + file)
        # check for beta/weird versions of roms and get rid of them
        # we want to do this for each zip file, that way we won't be traversing the whole directory twice
        for file in directory:
            if not file.endswith('.zip') and re.search('[*]', file):
                os.system('del ' + file)
