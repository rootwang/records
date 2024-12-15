# -*- coding: utf-8 -*-
"""
@File    : coroutine_1.py
@Author  : wangxin
@Date    : 2024/11/28
@Description: 底层实现
"""

def work1(n):
    i = 0
    while i < n:
        print("work1: i is {}".format(i))
        yield i
        i += 1

def work2(n):
    i = 0
    while i < n:
        print("work2: i is {}".format(i))
        yield i
        i += 1


if __name__ == '__main__':
    n = 10
    work1 = work1(n)
    work2 = work2(n)
    i = 0
    while i < n:
        next(work1)
        next(work2)
        i += 1
