# 捕获常规的异常
try:
    print('-----test--1---')
    open('123.txt','r')
    print('-----test--2---')
except Exception as e:
    print('捕获到异常',e)


print('*' * 100)

try:
    print(num)
except Exception as errorMsg:
    print('产生错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，真高兴')

print('*' * 100)

import time

try:
    f = open('123.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件的过程中，产生了异常，那么就会捕获到
        # 比如 按下了 ctrl+c
        pass
    finally:
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")
