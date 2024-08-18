# 创建进程池
# 进程池的原理
# 创建一个进程池, 设置进程池中最大的进程数量,假设进程池中最大的进程数目为3,现有10个人任务需要执行,那么进行一次执行3个任务,一共需要4次就能将全部任务执行完成
# 进程池对象 = Pool(N)

# 非阻塞式和阻塞式
# 前者时间节省
from multiprocessing import  Pool
import os
import time


def task(name):
    print(f'子进程的PID为:{os.getpid()}, 执行的任务:{name}')


if __name__ == '__main__':
    # 主进程
    start_time = time.time()
    print('主进程')

    # 创建进程池
    pool = Pool(3)
    for i in range(4):
        # 非阻塞式 时间少
        # pool.apply_async(func=task, args=(i, ))
        # 阻塞式 时间多
        pool.apply(func=task, args=(i,))

    # 关闭线性池不再接收任务
    pool.close()
    pool.join()
    print('所有子进程结束, 父进程执行结束')
    print('时间差:', time.time() - start_time)