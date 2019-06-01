import glob
import os
import shutil

path = input('folder path: ')
word = input('file-name contains: ')
# ext = input('file-extension: ')
ext = 'xml'
# dir_name = input('new folder name: ')
dir_name = word

file_paths = glob.glob(r'%s\**\*%s*.%s' % (path,word,ext), recursive=True)

d = r'%s\%s' % (path, dir_name)
os.mkdir(d)

for p in file_paths:
    shutil.copy(p, d)
