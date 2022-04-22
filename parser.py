#!/usr/bin/env python3
import javalang

with open('test.java', 'r') as file:
     data = file.read()
     tree = javalang.parse.parse(data)
print(tree)
