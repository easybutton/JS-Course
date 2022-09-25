# Script: list_path.py - lists each path directory on a line
import os
rawpath = os.environ['PATH']

if ':' in rawpath:           # Unix path
    path = rawpath.split(':')

if ';' in rawpath:           # Windows path
    path = rawpath.split(';')

for p in path:
    print(p)

