# 函数式创建线程
# thread = Thread(一系列参数)

import threading
from threading import Thread, Lock
import time
import random


class Account:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.lock = threading.Lock()

    # 存款
    def d(self, amount):
        with self.lock:
            self.balance += amount
            log(f"存款: {amount} 到 {self.name}, 余额: {self.balance}")

    # 取款
    def q(self, amount):
        with self.lock:
            if self.balance > amount:
                self.balance -= amount
                log(f"取款: {amount} 从 {self.name}, 余额: {self.balance}")
            else:
                log(f"余额不足")

    # 转账
    def f(self, target, amount):
        with self.lock:
            if self.balance > amount:
                self.balance = - amount
                target.d(amount)
                log(f"转账: {amount} 从 {self.name} 到 {target.name}, 余额: {self.balance}")
            else:
                log(f'转账失败')


def log(message):
    with log_lock:
        print(f"[{time.strftime('%H:%M:%S')}] {message}")


def func(accounts):
    for _ in range(2):
        account = random.choice(accounts)
        operation = random.choice(['d', 'q', 'f'])
        amount = random.randint(1, 100)

        if operation == 'd':
            account.d(amount)
        elif operation == 'q':
            account.q(amount)
        elif operation == 'f':
            target = random.choice([acc for acc in accounts if acc != account])
            account.f(target, amount)


if __name__ == '__main__':
    # 创建日志锁
    log_lock = threading.Lock()

    # 创建账户
    A = Account('AA', 1000)
    B = Account('BB', 1000)
    C = Account('CC', 1000)
    accounts = [A, B, C]

    # 创建线程
    lst = []
    for _ in range(3):
        t = threading.Thread(target=func, args=(accounts,))
        t.start()
        lst.append(t)

    # 等待所有线程完成
    for i in lst:
        i.join()

    for account in accounts:
        print(f"{account.name}的钱{account.balance}")


