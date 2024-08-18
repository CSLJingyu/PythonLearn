# 生产者和消费者
# 生产者生成数据放在中间仓库
# 消费者从中间仓库提取出数据

# 实现消费者和生产者
from queue import Queue
from threading import Thread
import time


# 创建生产者
class Producer(Thread):

    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for i in range(1, 6):
            print(f'生产者线程:{self.name}将产品{i}放在队列中')
            self.queue.put(i)
            time.sleep(2)

        print('生产者完成了所有的生产数据的存放')


# 创建消费者
class Consumer(Thread):

    def __init__(self, name, queue):
        Thread.__init__(self, name=name)
        self.queue = queue

    def run(self):
        for _ in range(5):
            # 取出中间仓库的数据
            # 如果队列中没有数据,那么get()方法会阻塞消费线程,一直到有数据的时候才会执行
            # 当生产者放入生成的数据后,消费者线程会立即从队列中取出改数据
            value = self.queue.get()
            print(f"消费者线程:{self.name}取出了{value}")

        print('消费者完成了所有的生产数据的取出')


if __name__ == '__main__':
    # 创建队列
    queue = Queue()

    # 创建生产者
    p = Producer('Producer', queue)
    # 创建消费者
    c = Consumer('Consumer', queue)

    # 启动线程
    p.start()
    c.start()

    # 阻塞
    p.join()
    c.join()

    print('--主线程结束---')



