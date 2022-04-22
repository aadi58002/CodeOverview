#!/usr/bin/env python3
import os
import sys

def checkfiles(prefixpath):
    for file in os.listdir(path):
        if os.path.isfile(file) and file.endswith('.java'):
            print(file)
        elif os.path.isdir(file):
            path = file
            checkfiles(path)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Must give a directory from where to serve the files")
        exit(1)

    path = sys.argv[1]
    checkfiles(path)
