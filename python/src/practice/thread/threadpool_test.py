# -*- coding: utf-8 -*-
"""
@File    : threadpool_test.py
@Author  : wangxin
@Date    : 2024/11/25
@Description: 
"""

from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


if __name__ == '__main__':
    # 方式一：
    # executor = ThreadPoolExecutor(max_workers=3)
    # task1 = executor.submit(get_html, (3))
    # task2 = executor.submit(get_html, (5))
    #
    # time.sleep(10)
    # print(task1.done())
    # print(task2.done())
    # print(task1.cancel()) # 只有提交前取消才可以停止
    # print("result is {}".format(task1.result()))

    # 方式二：推荐
    with ThreadPoolExecutor(max_workers=3) as executor:
        all_task = [executor.submit(get_html, (i)) for i in range(5)]
        # wait(all_task, return_when=FIRST_COMPLETED)
        for future in as_completed(all_task):
            data = future.result()
            print("get result of {}".format(data))