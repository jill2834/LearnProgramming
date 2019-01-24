#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:24:16 2019

@author: Jill
"""

for i in range(1, 10):
    for j in range(1, i+1):
        result = i*j
        # No wrap add space at the end of the line
        print('%d*%d=%d' % (i, j, result), end=' ')
    print()  # print along with the order of i


def print_pyramid(max_level):
    for current_level in range(1, max_level+1):
        for i in range(max_level - current_level):
            print(' ', end=' ')
        for j in range(2*current_level - 1):
            print('*', end=' ')
        print()


if __name__ == '__main__':
    max_level = 5
    print_pyramid(max_level)


name = 'Albert say hello'
print(name.find('o', 1, 3))
print(name.count('A',1,2))
print(name.center(30,'-'))
print(name.ljust(30,'*'))
print(name.rjust(30,'*'))
print(name.zfill(50))

l1 = {
    'name': 'albert',
    'age': 18,
    'gender': 'male'
}

res = l1.pop('name') 
print(res)
print(l1)

res2 = l1.popitem()

d1 = {
    'name': 'albert',
    'age': 18,
}
d1.setdefault('name', 'Albert')
d1.setdefault('gender', 'male')
print(d1)

pythons={'albert','孙悟空','周星驰','朱茵','林志玲'}
ais={'猪八戒','郭德纲', '林忆莲', '周星驰'}

print(pythons & ais)
print(pythons | ais)
print(pythons - ais)
print(pythons ^ ais)

l=['a','b',1,'a','a']
new_l = set(l)
print(new_l)


l1 = []
l=['a','b',1,'a','a']
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

l1 = []
s = set()
for i in l:
    if i not in s:
        s.add(i)
        print(s)
        l1.append(i)
        print(l1)
print(l1)


l=[
    {'name':'albert','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'alex','age':20,'sex':'female'},
    {'name':'albert','age':18,'sex':'male'},
    {'name':'albert','age':18,'sex':'male'},
]


s = set()
l1 = []
for item in l:
    val = (item['name'], item['age'], item['sex'])
    if val not in s:
        s.add(val)
        l1.append(item)
print(l1)

l1 = []
for item in l:
    if item not in l1:
        l1.append(item)
print(l1)