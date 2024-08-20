# 在数据共享的情况下, 通过锁来实现线程之间的先后争取资源的顺序
import threading
from threading import Thread, Lock
import time

ticket = 50

# 创建一个锁对象
lock = Lock()


def scale_ticket():
    global ticket

    # 假设每个排队的窗口有100人
    for i in range(100):  # 每个线程执行100次循环
        # 获取锁
        lock.acquire()
        with lock:
            if ticket > 0:
                print(f'{threading.currentThread().name}正在卖第{ticket}张票')
                ticket -= 1

        time.sleep(1)
        # 释放锁
        lock.release()


if __name__ == '__main__':
    # 创建三个线程,表示含有三个窗口
    for i in range(3):
        t = Thread(target=scale_ticket)
        t.start()


    print('主线程结束')
