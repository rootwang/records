# -*- coding: utf-8 -*-
"""
@File    : coroutine_greenlet.py
@Author  : wangxin
@Date    : 2024/11/28
@Description: 使用greenlet来实现协程
"""

from greenlet import greenlet


def work1(n):
    i = 0
    while i < n:
        print("work1: i is {}".format(i))
        i += 1
        g2.switch(n)


def work2(n):
    i = 0
    while i < n:
        print("work2: i is {}".format(i))
        i += 1
        g1.switch(n)


if __name__ == '__main__':
    n = 10
    g2 = greenlet(work2)
    g1 = greenlet(work1)

    g1.switch(n)