#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 18:06:13 2018

@author: Jill
"""


# 03/12/2018
# Question 1
a = 'hello'
a = list(a)
a.reverse()
a = ''.join(a)


a = input('Please enter your input: ')
a = list(a)
c = []
for i in range(len(a)):
    b = list.pop(a)
    c.insert(i, b)
c = ''.join(c)


# Question 2
n = 15
d = []
for i in range(1, n+1):
    if i > 0:
        if i % 3 == 0:
            if i % 5 == 0:
                i = str(i)
                i = 'FizzBuzz'
            else:
                i = str(i)
                i = 'Fizz'
        elif i % 5 == 0:
            i = str(i)
            i = 'Buzz'
        else:
            i = str(i)
    d.append(i)


# 04/12/2018
# Question 1
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


# Question 2
a = [4, 1, 2, 1, 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        b.remove(i)
for j in b:
    print(j)

hash_table = {}
for i in a:
    try:
        hash_table.pop(i)
    except:
        hash_table[i] = 1
hash_table.popitem()[0]


a = [0, 1, 0, 3, 12]
b = a.count(0)
while 0 in a:
    a.remove(0)
n = 0
while n < b:
    a.append(0)
    n += 1
print(a)

zero = 0
for i in range(len(a)):
    if a[i] != 0:
        a[i], a[zero] = a[zero], a[i]
        zero += 1






            

    