import string
import random
import os


# 批量创建文件
good = ['apple', 'pile', 'smoke', 'egg']
for i in range(3):
    random_element = random.choice(good)

    user_id = ''.join(random.choices('0123456789abcdef', k=9))
    f = open(f'./{i:03}_{random_element}_{user_id}.txt', 'w')
    f.write("")
    f.close()


# 批量创建文件夹
def mkdir(path, nums):
    for i in range(nums):
        os.mkdir(path + '/' + str(i))


if __name__ == '__main__':
    path = './new_dir'
    if not os.path.exists(path):
        os.mkdir(path)

    print('输入创建的个数:', end=" ")
    nums = int(input())
    mkdir(path, nums)
