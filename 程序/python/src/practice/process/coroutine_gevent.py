# -*- coding: utf-8 -*-
"""
@File    : coroutine_gevent.py
@Author  : wangxin
@Date    : 2024/11/28
@Description: gevent 自动切换协程
"""

import gevent, time

def work1(n):
    i = 0
    while i < n:
        print("work1: i is {}".format(i))
        i += 1
        gevent.sleep(1)
        # time.sleep(1)  # 不能用这个,因为不能被gevent认可 ，方式二就是破解
        # 在最前面加上 from gevent import monkey
        # monkey.patch_all()


def work2(n):
    i = 0
    while i < n:
        print("work2: i is {}".format(i))
        i += 1
        gevent.sleep(1)


if __name__ == '__main__':
    n = 10

    g1 = gevent.spawn(work1, 10)
    g2 = gevent.spawn(work2, 10)

    g1.join()
    g2.join()