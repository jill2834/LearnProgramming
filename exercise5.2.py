#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 11:42:32 2019

@author: Jill
"""


import time
import os
import sys

if len(sys.argv):
    filename = sys.argv[1]
    if not filename:
        print('Please provide a file that you want to monitor')
        sys.exit()
else:
    print('Please provide a parameter to specify filename')
    sys.exit()

if not os.path.isfile(filename):
    print('Please provide a valid filename')
    sys.exit()


def tail(filename):
    with open(filename, 'r') as f:
        f.seek(0, 2)  # locate to the end of the file
            while True:
                line = f.readline()
                    if not line:
                        time.sleep(0.1)
                        continue
                    yield line


try:
    for line in tail(filename):
        print(line)
except KeyboardInterrupe as Keys:
    sys.exit()
    
