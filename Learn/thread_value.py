# 线程之间的数据是可以共享的

import threading
from threading import Thread
import time

a = 100


def add():
    print('加线程开始')
    global a
    a = a + 100
    print('加线程后a的数值:', a)
    print('加线程结束')


def sub():
    print('减线程开始')
    global a
    a = a - 20
    print('减线程后a的数值:', a)
    print('减线程结束')


if __name__ == '__main__':
    # 父线程
    print('主线程开始')
    print("一开始a的数值:", a)

    # 加线程
    add = Thread(target=add)

    # 减线程
    sub = Thread(target=sub)

    add.start()
    sub.start()
    add.join()
    sub.join()

    print("结束时a的数值:", a)
    print('主线程结束')


