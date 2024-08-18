# 创建进程的方式
from multiprocessing import Process
import os
import time


def sub_process1(name):
    print(f"子进程PID:{os.getpid()}, 父进程的PID:{os.getppid()}, ------{name}")
    time.sleep(2)


def sub_process2(name):
    print(f"子进程PID:{os.getpid()}, 父进程的PID:{os.getppid()}, ------{name}")
    time.sleep(2)


if __name__ == '__main__':
    # 主进程
    print('主进程开始')
    for i in range(3):
        # 创建第一个主进程
        p1 = Process(target=sub_process1, args=("ll",))
        # 创建第二个主进程
        p2 = Process(target=sub_process2, args=("kk",))

        # 启动子进程
        p1.start()
        p2.start()

        # 查看是否活跃
        print(p1.name, '是否执行活跃', p1.is_alive())
        print(p2.name, '是否执行活跃', p2.is_alive())

        print(p1.name, 'pid是', p1.pid)
        print(p2.name, 'pid是', p2.pid)

        # 执行子进程
        p1.join()
        p2.join()

        # 执行完成查看是否活跃
        print(p1.name, '是否执行活跃', p1.is_alive())
        print(p2.name, '是否执行活跃', p2.is_alive())

        print("-" * 50)

    print('主进程执行完成')
