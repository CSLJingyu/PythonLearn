# 创建进程的方式
from multiprocessing import Process
import os
import time


def sub_process1(name):
    print(f"子进程PID:{os.getpid()}, 父进程的PID:{os.getppid()}, ------{name}")
    time.sleep(2)


def sub_process2(name):
    print(f"子进程PID:{os.getpid()}, 父进程的PID:{os.getppid()}, ------{name}")


if __name__ == '__main__':
    # 主进程
    print('主进程')
    for i in range(3):
        # 创建子进程
        p1 = Process(target=sub_process1, args=('ll', ))
        p2 = Process(target=sub_process2, args=('kk',))

        p1.start()
        p1.join()

        p2.start()
        p2.join()

        # 终止进程
        p1.terminate()
        p2.terminate()

        print('-' * 50)

    print('主进程结束')
