# 函数式创建线程
# thread = Thread(一系列参数)

import threading
from threading import Thread
import time


# 线程执行的函数
def task():
    for i in range(3):
        time.sleep(3)
        print(f"线程名:{threading.currentThread().name}正在执行{i}", end="\n")


if __name__ == '__main__':
    start = time.time()
    print('主线程开始')

    # 创建线程
    lst = [Thread(target=task) for i in range(2)]

    for item in lst:
        # 启动线程
        item.start()

    for item in lst:
        # 阻塞
        item.join()

    print('耗时:', time.time() - start)


# 一共有三个线程, 一个主线程, 两个子线程
# 并发执行 线程1,2的执行顺序是随机的
