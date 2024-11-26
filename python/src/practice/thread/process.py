# -*- coding: utf-8 -*-
"""
@File    : process.py
@Author  : wangxin
@Date    : 2024/11/26
@Description: 多进程编程
"""

import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        all_task = [executor.submit(get_html, (i)) for i in range(5)]
        # wait(all_task, return_when=FIRST_COMPLETED)
        for future in as_completed(all_task):
            data = future.result()
            print("get result of {}".format(data))