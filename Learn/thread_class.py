# 继承式创建线程
# thread = Thread(一系列参数)

import threading
from threading import Thread
import time


class SubThread(Thread):

    def __init__(self, name):
        super().__init__()  # 调用父类的 __init__ 方法，确保线程正常初始化
        self.name = name

    def run(self):
        for i in range(3):
            time.sleep(3)
            print(f"线程名:{threading.currentThread().name}正在执行{i}", end="\n")


if __name__ == '__main__':
    print('主线程开始')
    start = time.time()

    # 创建线程
    lst = [SubThread(f"线程-{i}") for i in range(2)]

    for item in lst:
        # 启动线程
        item.start()

    for item in lst:
        # 阻塞
        item.join()

    print('耗时:', time.time() - start)