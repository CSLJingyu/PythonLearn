# 进程之间的通信----队列
from multiprocessing import Queue

if __name__ == '__main__':
    # 创建队列
    # 队列长度最大长度为3
    queue = Queue(3)
    print('队列是否为空', queue.empty())
    print('队列是否为满', queue.full())

    # 向队列中插入元素
    queue.put('element 1')
    queue.put('element 2')
    print('队列是否为空', queue.empty())
    print('队列是否为满', queue.full())
    print('当前队列消息个数', queue.qsize())
    # put和put_nowait的区别就是
    # 前者是默认block为True, 等到有队列有空位,要是没有的不会直接报错
    # 后者是默认block为False, 立即要求队列队列是否有空位, 要是没有的就直接报错

    # 出队
    print('出队', queue.get())
    queue.put('element_3')
    print('当前队列元素个数', queue.qsize())
    queue.put_nowait('element_4')
    print('当前队列元素个数', queue.qsize())
    #queue.put_nowait('element_5')

    # 遍历出队
    if not queue.empty():
        for item in range(queue.qsize()):
            # nowait不会等待
            print(queue.get_nowait())


