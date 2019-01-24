#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:59:01 2019

@author: Jill
"""


import os


path = '/Users/Jill/Documents/LearnProgramming/'

os.getcwd()
os.chdir(path)


total_price = 0
with open('a.txt', 'r', encoding='utf-8') as f:
    for line in f:
        price = int(line.split()[1]) * int(line.split()[2])
        total_price += price
    print(total_price)


with open('a.txt', 'r') as read_f, open('.a.txt.swap', 'w') as write_f:
    for line in read_f:
        line = line.replace('mac', 'linux')
        write_f.write(line)

os.rename('.a.txt.swap', 'a2.txt')
