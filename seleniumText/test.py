#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 16:01
# @Author  : Bwcheng
# @Site    : 
# @File    : test.py
# @Software: PyCharm

def getValue(*key):
    print(key)

def d(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    getValue('1', '2')
    d(*(1, 2, 3)) # 相当于d(1, 2, 3)  如果是d(1, 2, 3)就会报错