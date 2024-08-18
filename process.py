# 创建进程的方式为多种多样
# Process(group=None, target=None, name=None, args=(), kwargs={}, daemon=None)  target为必须传入的参数, 这个参数一般为函数名; args是函数的参数,用元组的形式传入;

from multiprocessing import Process
import os
import time


# 1.使用函数的方式创建进程
def test():
    print(f"我是子进程,PID为:{os.getpid()}, 我的父进程PID为{os.getppid()}")
    time.sleep(2)


if __name__ == '__main__':
    print('主进程开始执行')
    lst = []

    # 创建3个子进程
    for i in range(3):
        # 创建子进程
        p = Process(target=test)
        # 启动子进程
        p.start()
        # 启动中将进程添加到列表中
        lst.append(p)

    # 遍历lst, 等待所有子进程完成
    for item in lst:
        # 阻塞主进程
        item.join()

    # 主进程要等到所有子进程结束后,才会执行
    print('主进程执行结束')
