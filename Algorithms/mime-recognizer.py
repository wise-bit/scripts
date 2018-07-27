# Folder reader yet to be implemented

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
arr = []
d = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    d[ext.lower()] = mt
for i in range(q):
    try:
        fname = input()
        array = fname.split(".") # One file name per line.
        name = array[-1]
        arr.append(fname)
        if name.lower() in d.keys() and len(array) > 1:
            print(d[name.lower()])
        else:
            print("UNKNOWN")
    except Exception as e:
        print("UNKNOWN" + e)
