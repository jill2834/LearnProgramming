#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:04:50 2019

@author: Jill
"""


def login(account):
    count = 0
    flag = 1
    while flag:
            input_name = input('Please enter your name: ')
            input_passwd = input('Please enter your password: ')
            if input_name not in account.keys() or input_passwd not in account.values():
                count += 1
                if count == 3:
                    print('Invalid account')
                    flag = 0
            elif input_name in account.keys() and input_passwd in account.values():
                print('Welcome')
                flag = 0


if __name__ == '__main__':
    name = ['Harry', 'Julie', 'Amy']
    passwd = ['1765432', 'bchjanxj', 'nxjsn1234']
    account = dict(zip(name, passwd))
    login(account)
