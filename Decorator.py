# 闭包
# 函数嵌套下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,使用外部函数变量的内部函数叫做闭包
import time


def func1(num1: int):
    def func2(num2: int):
        # 内部函数使用了外部函数的变量
        # print(f"num1: {num1}; num2: {num2}")
        res_inner = num1 + num2
        # print('res_inner: ', res_inner)

    # 返回的是一个函数
    return func2


# 创建闭包实例
# 此时的res是func2函数 res记住了传入的参数num1为10
res = func1(10)
# 执行闭包
# 这里实际是调用fun2(6)
res(6)  # 得到16


# 闭包修改外部函数变量的数值
def func1(num1: int):
    def func2(num2: int):
        # 声明num1是来在外层函数的变量
        nonlocal num1
        num1 = 8
        # 内部函数使用外部函数的变量
        num1 = num2 + num1
        # print(f"num1:{num1}")

    # 外部函数返回内部函数
    return func2


# 创建闭包实例
f = func1(10)  # 将传入的num1=10变为了8
# 执行闭包
f(6)  # 得到14
# print('*' * 50)
print()


# 装饰器
# 等价于以一个函数作为参数传递给闭包中的外部函数, 同时在内部函数中使用这个函数, 并且添加新的功能
# 外部函数只能有一个参数,一般是被装饰的函数
# 内部函数可以依据被装饰的函数提供多个参数以及返回值

# 以下是简单的例子展示函数名作为参数进行传递
def baiyu():
    t1 = time.time()
    print('1')
    time.sleep(1)
    print(f'total time: {time.time() - t1}')


def blog(name):
    t1 = time.time()
    print('进入blog函数')
    name()
    print('我的世界')
    print(f"total time: {time.time() - t1}")


# 将上面的过程写为一个简单的装饰器
def baifu_1():
    print('1')
    time.sleep(1)


# 定义了一个计算函数运行时间的修饰器
# wrapper函数体就是实现装饰器的内容
def count_time(function):
    def wrapper():
        t1 = time.time()
        function()
        print(f'total time: {time.time() - t1}')

    # 返回的是一个函数
    return wrapper


# 装饰器语法糖
def count_time1(function):
    def wrapper():
        t1 = time.time()
        function()
        print(f'total time: {time.time() - t1}')

    return wrapper


@count_time1
# 这个@count_time1是装饰器的语法糖
def baidu():
    print('baidu')
    time.sleep(1)


####################################################################################
# 装饰器传参
# 此时装饰器需要优化,修改为可以接受任意参数的装饰器

def count_blog(function):
    # 可以接受任意参数的装饰器
    def wrapper(*args, **kwargs):
        t1 = time.time()
        function(*args, **kwargs)
        print('执行时间为:', time.time() - t1)

    return wrapper


# 语法糖写
@count_blog
def blog_name(name):
    print('进入blog_name函数')
    name()
    print('OK')


####################################################################################

####################################################################################
# 带参数的装饰器
# 装饰器函数也是函数,是函数就可以实现传参操作
# 在基于原来的函数外部添加一个函数,这样接收回来的参数就可以在内部的函数里面进行调用
# 下面的例子中,传入了备用信息msg

def count_time_args(msg=None):
    def count_time(function):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            function(*args, **kwargs)
            print(f"{msg}的执行时间为: {time.time() - t1}")

        return wrapper

    return count_time


@count_time_args(msg="baidu")
def fun_one():
    time.sleep(1)


@count_time_args(msg="wangyi")
def fun_two():
    time.sleep(1)


####################################################################################
# 自己写的测试
def x(function):
    def wrapper(*args, **kwargs):
        print('OK')
        function(*args, **kwargs)
        print('No')

    return wrapper


@x
def y(x: int, y: str):
    print("*" * 50)
    print('x is ', x)
    print('y is ', y)
    print("*" * 50)


####################################################################################


####################################################################################
# 类装饰器
# 类的装饰器的实现是调用了类里面的__call__函数
# 将一个类作为装饰器的时候,工作流程如下所示:
# 1.通过__init__() 方法初始类
# 2.通过__call__() 方法调用真正的装饰方法
# 每调用一次修饰器,就会执行修饰器里面的__init__(self, function)函数

class BaiduDecorator:
    def __init__(self, function):
        self.function = function
        print('执行BaiduDecorator类的__init__')

    def __call__(self, *args, **kwargs):
        print('进入BaiduDecorator的__call__函数')
        t1 = time.time()
        self.function(*args, **kwargs)
        print('执行时间为: ', time.time() - t1)


@BaiduDecorator
def baifu():
    print("百度")
    time.sleep(1)


def something():
    time.sleep(5)
    print('i am a people')


@BaiduDecorator
def blog_somthing(name):
    print('进入blog函数')
    name()
    print('输出一些美好的东西')


####################################################################################

####################################################################################
# 带参数的装饰器
# 当装饰器有参数的时候,__init__()函数就不能传入function(这个是表示要传入的参数) 而function是在__call__函数调用的时候传入
class IDecorator:
    def __init__(self, arg1, arg2):
        print('执行IDecorator类的__init__()方法')
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        print('执行IDecorator类的__call__()方法')

        def i_wrapper(*args):
            print('执行wrapper()')
            print('装饰器的参数: ', self.arg1, self.arg2)
            print('执行 ' + func.__name__ + '()')
            func(*args)  # 传入的参数是args1, args2, args3
            print(func.__name__ + '()执行完成')

        return i_wrapper


@IDecorator('hello', 'nihao')
def example(args1, args2, args3):
    print('传入的example()的三个参数:', args1, args2, args3)


####################################################################################

####################################################################################
# 装饰器的顺序
# 一个函数可以被多个装饰器进行装饰,装饰器之间存在一定的顺序
# 在执行的时候,实现的是先执行原来函数的功能, 然后就近原则从下到上一次执行装饰器的内容
def YouDecorator_1(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('YouDecorator_1')

    return wrapper


def YouDecorator_2(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('YouDecorator_2')

    return wrapper


def YouDecorator_3(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('YouDecorator_3')

    return wrapper


@YouDecorator_1
@YouDecorator_2
@YouDecorator_3
def You():
    print('You are beautiful!!!')


####################################################################################


if __name__ == '__main__':
    # func = baiyu  # 将baiyu这个函数名赋值给变量func
    # func()  # 执行func函数
    # print('*' * 50)
    # blog(baiyu)  # 将baiyu函数名作为参数复传递给blog函数
    #
    # print('#' * 50)
    # print('修饰器的使用')
    # baifu_1 = count_time(baifu_1)  # 装饰器count_time(baiyu_1) 返回的对象是一个wrapper, 这条语句就说等价于 baifu_1 = wrapper
    # baifu_1()  # 执行baiyu_1()等价于执行内部函数wrapper()
    # print('#' * 50)
    # print()

    # 使用了语法糖后, 就不用写baifu_1 = count_time(baifu_1), 因为经过语法糖的处理 默认的传人参数是被装饰的函数
    # baidu()

    # 用到了语法糖, 将baidu这个函数传入到blog_name中,然后进行count_name处理
    # blog_name(baidu)

    # 装饰器带参数
    # fun_one()
    # fun_two()

    # 测试 传入普通的变量
    # y(12, "changer")

    # 类的装饰器
    # baifu()是BaiduDecorator的实例, 调用baifu()就是等于调用这个__call__方法
    # baifu()
    # blog_somthing(something)

    # 带参数的类装饰器
    # print('开始调用example函数')
    # example('i', 'you', 'he')
    # print('结束函数')

    print("*" * 50)
    You()
