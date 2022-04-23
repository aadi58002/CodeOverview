#!/usr/bin/env python3

import os
import sys
import javalang
import shutil
from jinja2 import Environment, FileSystemLoader, select_autoescape

def parser(file_name) :
    with open(file_name,'r') as file:
        data = file.read()
        tree = javalang.parse.parse(data)
    return tree

def search_files(directory, extension):
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(directory):
        dirs_list = [
                os.path.join(dirpath, dirname).removeprefix("./") + "/"
                for dirname in dirnames
                if not dirpath.startswith("./.") and not dirname.startswith(".")
        ]
        files_list = [
                os.path.join(dirpath, name).removeprefix("./")
                for name in files
                if not dirpath.startswith("./.") and name.endswith(extension)
        ]
        for path in files_list:
            createhtml(path, dirs_list, files_list)

def createhtml(file, dirs_list, files_list):
    print("Generating for", file)
    cache_path = ".code-cache"
    os.makedirs(cache_path, exist_ok=True)
    shutil.copy("./template.css", os.path.join(cache_path, "template.css"))

    htmlfilepath = os.path.join(cache_path, os.path.join(os.path.dirname(file), "index.html"))
    html = template.render(nav_dir_list=dirs_list, nav_file_list=[os.path.splitext(f)[0] for f in files_list])
    os.makedirs(os.path.dirname(htmlfilepath), exist_ok=True)
    print(htmlfilepath)
    with open(htmlfilepath, 'w') as htmlfile:
        htmlfile.write(html)

    htmlfilepath = os.path.join(cache_path, os.path.splitext(file)[0] + ".html")
    data = ['test data']
    html = template.render(nav_dir_list=dirs_list, nav_file_list=[os.path.splitext(f)[0] for f in files_list], filename=file, data=data)
    os.makedirs(os.path.dirname(htmlfilepath), exist_ok=True)
    print(htmlfilepath)
    with open(htmlfilepath, 'w') as htmlfile:
        htmlfile.write(html)

                createhtml(os.path.join(dirpath, name))
            elif not extension:
                print(os.path.join(dirpath, name))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Must give a directory from where to serve the files")
        exit()

    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape()
    )
    template = env.get_template("template.html")

    path = sys.argv[1]
    search_files(path,"java")
