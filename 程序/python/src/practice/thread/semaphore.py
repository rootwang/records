# -*- coding: utf-8 -*-
"""
@File    : semaphore.py
@Author  : wangxin
@Date    : 2024/11/25
@Description: 用于控制一次执行线程的数量
"""
import threading
import time


class Student(threading.Thread):
    def __init__(self, name, sem):
        super().__init__()
        print("student {} in".format(name))
        self.name = name
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("the {} of student is done".format(self.name))
        self.sem.release()

class Study(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(10):
            self.sem.acquire()
            s_thread = Student("第 {} 个同学".format(i), self.sem)
            s_thread.start()


if __name__ == '__main__':
    sema = threading.Semaphore(2)
    study = Study(sema)
    study.start()
