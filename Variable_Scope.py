# 函数体内的变量 只会在函数体内部有效果
def func():
    var = 1000
    print(var)


func()

# global关键字
var = 200
def func1():
    # 声明var为全局变量
    global var
    var = 2100
    print(var)

func1()
print(var)  # 输出的数值为全局变量的数值 2100