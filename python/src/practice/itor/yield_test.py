# -*- coding: utf-8 -*-
"""
@File    : yield_test.py
@Author  : wangxin
@Date    : 2024/11/25
@Description: yield = return + 上次执行的地方继续执行
"""


def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)
