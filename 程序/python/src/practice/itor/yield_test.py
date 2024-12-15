# -*- coding: utf-8 -*-
"""
@File    : yield_test.py
@Author  : wangxin
@Date    : 2024/11/25
@Description: yield = return + 上次执行的地方继续执行
"""
import send


# 例子1
# def foo(num):
#     print("starting...")
#     while num<10:
#         num=num+1
#         yield num
#
# if __name__ == '__main__':
#     for n in foo(2):
#         print(n)

# 例子2:菲波那契数列
def fibnacci(n):
    a, b = 1, 1
    current_index = 0
    print("------1111-------")
    while current_index < n:
        data = a
        a, b = b, a + b
        current_index += 1
        print("current_index is {} and a is {} and b is {} and data is {}".format(current_index, a, b, data))
        xxx = yield data
        print("------33333------")

        if xxx == 1:
            return "hahahahahahaha"

if __name__ == '__main__':
    fib = fibnacci(10)
    value= next(fib)
    print("第0列的值为{}".format(value))
    try:
        value = next(fib)
        print("第一列的值为{}".format(value))
        # 这里send一个1，可以传输一个值到yield，比如上面的xxx，return会传回来一个异常回来
        value = fib.send(1)
        print("第二列的值为{}".format(value))
    except Exception as e:
        print(e)
    print(next(fib))










