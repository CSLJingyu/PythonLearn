# 创建进程的方式
from multiprocessing import Process
import os
import time


# 通过类继承的形式重写子进程
class SubProcess(Process):

    def __init__(self, name):
        super().__init__()
        self.name = name

    # 重写父类中的run方法
    def run(self):
        print(f"子进程的名字：{self.name}, PID:{os.getpid()}, FPID:{os.getppid()}")


if __name__ == '__main__':
    # 主进程
    print('主进程开始')

    # 创建子进程
    for i in range(1, 4):
        subprocess = SubProcess(f"{i}")

        subprocess.start()
        subprocess.join()
        subprocess.terminate()

    print('主进程结束')


