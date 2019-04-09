import fnmatch
import os

os.system('pip install -r requirements.txt')
 
rootPath = '/'
pattern = '*.mp3'
 
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))