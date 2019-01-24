#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 12:19:00 2019

@author: Jill
"""

result = 0
for i in range(100):
    if i % 2 == 1:
        result += i
    else:
        pass


count = 1
result = 0
while count <= 100:
    if count % 2 != 0:
       result += count
    count+=1
    

def find_index(a, n, key):
    i = 0
    if a is None or n <= 0:
        return -1
    while i < n:
        if a[i] == key:
            return i
        i += 1
    return -1

a = [4, 2, 3, 5, 9, 6]
n = len(a)
find_index(a, n, key)
    
 