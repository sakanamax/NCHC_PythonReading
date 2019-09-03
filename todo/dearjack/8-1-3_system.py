import os
import shutil

#os.system('ls -l')
shutil.copyfileobj(open('zop.txt','r'), open('zop1.txt', 'w'))