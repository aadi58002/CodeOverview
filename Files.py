#!/usr/bin/env python3
import os
import sys

n = len(sys.argv)
if n != 2:
    exit ()

path = sys.argv[1]
def checkfiles (path) :
    files_list = os.listdir(path)
    for file in files_list :
        if os.path.isfile(file) and file.endswith('.java') :
            print(file)
            # createhtml (file)
        elif os.path.isdir(file) :
            path = file
            checkfiles(path)

checkfiles(path)
