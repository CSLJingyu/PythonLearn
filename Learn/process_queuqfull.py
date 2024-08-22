# 进程之间的通信----队列
from multiprocessing import Queue, Process
import time
a = 100

def write_msg(queue):
    global a
    if not queue.full():
        for i in range(6):
            a = a - 10
            queue.put(a)
            print('a进队的数值:', a)


def read_msg(queue):
    time.sleep(1)
    while not queue.empty():
        print('a出队的数值:', queue.get())


if __name__ == '__main__':
    # 父进程
    print('开始执行父进程')
    # 没有指定数据 可以说接收的消息个数是没有上限的
    queue = Queue()
    # 创建两个子进程
    process1 = Process(target=write_msg, args=(queue, ))
    process2 = Process(target=read_msg, args=(queue,))

    process1.start()
    process1.join()

    process2.start()
    process2.join()

    print('父进程结束')


