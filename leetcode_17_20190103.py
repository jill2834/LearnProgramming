#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:46:11 2019

@author: Jill
"""


import string


def mapping_dics():
    q = []
    for i in string.ascii_lowercase:
        q.append(i)
    q = list(reversed(q))
    mapping_dic = {}
    for j in range(2, 10):
        b = []
        if j % 7 == 0 or j % 9 == 0:
            flag = 4
        else:
            flag = 3
        for x in range(flag):
            b.append(q.pop())
            mapping_dic[j] = b
    return mapping_dic


def mapping(digits):
    
    digit = mapping_dics()
    
    

c = ''
result = []
for y in d.keys():
    print('y', y)
    for z in d.keys():
        print('z', z)
        for i in range(len(d[y])):
            m = str(d[y][i])
            print('m', m)
        for j in range(len(d[z])):
            n = str(d[z][j])
            print('n', n)
        c = m + n
    result.append(c)
    
