import string
import random
import os
import time
from datetime import datetime


# 批量创建文件
# good = ['apple', 'pile', 'smoke', 'egg']
# for i in range(3):
#     random_element = random.choice(good)
#
#     user_id = ''.join(random.choices('0123456789abcdef', k=9))
#     f = open(f'./{i:03}_{random_element}_{user_id}.txt', 'w')
#     f.write("")
#     f.close()


# 批量创建文件夹
def mkdir(path, nums):
    for i in range(nums):
        os.mkdir(path + '/' + str(i))


# 记录用户登入日志并且查看
# 创建系统,每次登入时,将用户的登录日志写入文件,并且可以查看到用户的登入时间 用户名字

class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password


def show_info(user):
    user_name = user.name
    user_time = user.time


def random_name():
    lenth = random.randint(2, 4)
    name = ''.join(random.choices(string.ascii_letters, k=lenth))  # 随机生成汉字
    return name


def login_info(user):
    print('登录成功')
    with open('log.txt', 'a', encoding='utf-8') as file:
        s = f'用户名:{user.name}  登入时间{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
        file.write(s + '\n')


# 读日志
def get_login_information():
    with open('log.txt', "r", encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line ==  '':
                break
            else:
                print(line)


if __name__ == '__main__':
    lst = []
    for i in range(3):
        print('name:', end=" ")
        name = input()
        age = random.randint(18, 100)
        password = "password" + str(i)
        user = User(name, password)
        lst.append(user)

    for i in range(3):
        login_info(lst[i])
        time.sleep(1)

    get_login_information()

# if __name__ == '__main__':
#     path = './new_dir'
#     if not os.path.exists(path):
#         os.mkdir(path)
#
#     print('输入创建的个数:', end=" ")
#     nums = int(input())
#     mkdir(path, nums)
