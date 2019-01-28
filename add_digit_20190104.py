#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 16:09:30 2019

@author: Jill
"""


def addDigits(self, num):
    while num >= 10:
        num_mod = 0
        while num >= 0:
            num_mod += num % 10
            num = num // 10
        num = num_mod
    return num



def addDigits(self, num):
    if num < 10:
        return num
    else:
        num = num % 10 + self.addDigits(num // 10)
    return self.addDigits(num)







        


