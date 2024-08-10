# 多返回值用逗号隔开
def func():
    return 1, 2, 3


x, y, z = func()
print('x y z:', func()[0], func()[1], func()[2])


# 多种传参方式
# 1.位置参数
def user_info(name, age):
    print(f"{name}, {age}")


user_info('lcs', 26)


# 2.关键字参数是依据关键字进行传参的
# 位置参数必须在关键字参数前面
def user_info(name, age, x):
    print(f"{name}, {age}, {x}")


user_info(name='lcs', age=26, x=12)


# 3.缺身参数 就是默认参数, 没有传入的参数 但是自己有默认的数值
def x(name, age, gender="men"):
    print(f"{name}, {age}, {gender}")


x(name="lcs", age=12)


# 4.可变参数
# 用*号标记一个形式参数，以元组的方式来接受参数
def func(*args):
    print(args)


func('name', 'sex', 'age')  # 输出的是以元组的形式


# **kwargs表示参数，用字典的方式接受参数
def func(**kwargs):
    print(kwargs)


func(name='ly', age=12)  # 输出的是以字典的形式


# 函数作为传递的参数
def func():
    print("123")
    return "OK"


print(func())  # 输出函数的输出数值和返回值: 输出123 和返回值OK
# 函数可以和普通变量一样 实现赋值
func1 = func()  # 先是执行print('123')的命令 然后将返回值OK赋值给func1变量
print(func1)  # 输出的是func函数的返回值 OK
print('*' * 130)


# 函数作为参数进行传递
def add(x, y):
    return x + y


def compute(x, y, add):
    res = add(x, y)
    return res


x, y = 1, 9
def c(add):
    return add(x, y)


res = compute(1, 2, add)
print("res:", res)  # 输出3
print(c(add))   # 输出10


# lambda匿名函数 使用次数是一次
# lambda 传入参数: 函数体(单独一行代码表示一个函数的功能)
power = lambda x : x ** 2  # 此时的res作为一个函数了
ans = power(2)
print(ans)  # 输出4
# 常用排序
pairs = [(1, 'one'), (2, 'two'),(3, 'three'),(4, 'four'),]
sorted_pairs = sorted(pairs, key=lambda pair: pairs[1])   # 按照第二个关键字进行排序
# map函数 (函数名, 迭代对象)
list1 = [1, 2, 3]
power_list = list(map(lambda x : x**2, list1))
print(power_list)  # 输出[1, 4, 9]
print('*' * 130)

# 详细说明
def Add(x, y):
    return x + y

Add_1 = lambda x, y : x + y
res_Add = Add(1, 2)
res_Add1 = Add_1(1, 10)
print("res_Add:", res_Add)
print("res_Add1:", res_Add1)