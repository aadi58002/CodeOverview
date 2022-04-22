#!/usr/bin/env python3

import os
import sys
import javalang
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape

if len(sys.argv) != 2:
    print("Must give a directory from where to serve the files")
    exit()

def parser(file_name) :
    with open(file_name,'r') as file:
        data = file.read()
        tree = javalang.parse.parse(data)
    return tree

def search_files(directory, extension):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        files_list = [os.path.join(dirpath, dirname) for dirname in dirnames if not dirname.startswith(".")] + [os.path.join(dirpath, name) for name in files if name.endswith(extension)]
        for path in files_list:
            if extension and path.lower().endswith(extension):
                print(path)
                createhtml(path, files_list)
            elif not extension:
                print(path)

def createhtml(file, files_list):
    print(file)
    cache_path = ".code-cache"
    cssfilepath = os.path.join(cache_path, "template.css")
    shutil.copy("./template.css", cssfilepath)
    htmlfilepath = os.path.join(cache_path, os.path.splitext(file)[0] + ".html")
    os.makedirs(os.path.dirname(htmlfilepath), exist_ok=True)
    html = template.render(files_list=files_list)
    with open(htmlfilepath, 'w') as htmlfile:
        htmlfile.write(html)

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)
template = env.get_template("template.html")

path = sys.argv[1]
search_files(path,"java")
