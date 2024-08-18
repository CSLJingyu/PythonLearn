# 进程之间的数据是不会共享的
from multiprocessing import Process
import os
import time

a = 100


def add():
    print('加进程开始')
    global a
    a = a + 100
    print('加进程后a的数值:', a)
    print('加进程结束')


def sub():
    print('减进程开始')
    global a
    a = a - 20
    print('减进程后a的数值:', a)
    print('加进程结束')


if __name__ == '__main__':
    # 父进程
    print('主进程开始')

    # 加进程
    add_process = Process(target=add)
    add_process.start()
    add_process.join()
    print('a的数值:', a)

    print('-' * 50)

    # 减进程
    sub_process = Process(target=sub)
    sub_process.start()
    sub_process.join()
    print('a的数值:', a)

    print('主进程结束')