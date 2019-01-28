#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:01:37 2019

@author: Jill
"""

import copy


def get_mul_factor(num, result=[]):
    if(num == 1):
        total = copy.copy(result)
        if 1 not in total:
            total.append(1)
            print(total)
        elif(num < 1):
            return
        else:
            n = list(range(num+1))
            n.reverse()
            if 1 in result:
                m = range(len(n)-2)
            else:
                m = range(len(n)-1)
            for i in m:
                new_result = copy.copy(result)
                if num % n[i] == 0:
                    new_result.append(n[i])


if __name__ == '__main__':
    get_mul_factor(2)

        
            
        