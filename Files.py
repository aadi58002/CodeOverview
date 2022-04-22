#!/usr/bin/env python3
import os
import sys


def createhtml (base_java_file) :




n = len(sys.argv)
if n != 1:
    exit ()

path = sys.argv[0]
files_list = os.listdir(path)

for file in files_list :
    if os.path.isfile(file) and file.endswith('.java') :
        createhtml (file)
