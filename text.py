# 为什么使用装饰器
def func1():
    print('func1')


def name_func1(func1):
    print('into name_func1')
    func1()
    print('end func1')


# 简单的装饰器

def func2():
    print('func2()')


def decorator(function):
    def wrapper():
        print('into wrapper')
        function()
        print('end wrapper')

    return wrapper


# 装饰器的语法糖
def decorator(function):
    def wrapper():
        print('into wrapper')
        function()
        print('end wrapper')

    return wrapper


@decorator
def func3():
    print('func3()')


# 装饰器传参
def decorator(function):
    def wrapper(*args, **kwargs):
        print('into wrapper')
        function(*args, **kwargs)
        print('end wrapper')

    return wrapper


@decorator
def func4(x: int):
    print(f"{x} is right ")


# 带参数的装饰器
def now(msg):
    def decorator(function):
        def wrapper(*args, **kwargs):
            print(f'msg is {msg}')
            print('intp wrapper')
            function(*args)
            print('end wrapper')

        return wrapper

    return decorator


@now(msg='ok')
def func5(x: int):
    print(f"{x} is five")


# 类装饰器
class X:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print('into __call__方法')
        self.function(*args, **kwargs)
        print('end __call__方法')


@X
def func6(x: int):
    print(f'{x} is 6')


# 带参数的类装饰器
class Y:
    def __init__(self, args1, args2):
        self.args1 = args1
        self.args2 = args2

    def __call__(self, function):
        print('into __call__方法')

        def wrapper(*args):
            print('into wrapper')
            function(*args)
            print('end wrapper')

        return wrapper


@Y(23, 34)
def func7(x: int, y: int):
    print(f"{x} is func7")


func7(34, 344)
