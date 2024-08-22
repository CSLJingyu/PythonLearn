# 抽象类
# 必须包含大于等于一个的抽象方法，也可以包含普通的方法
# 抽象类的抽象方法不在类中实现
# 抽象类不可以被实例化
# 抽象类的子类要想进行实例化,必须先实现父类中的全部抽象方法

# 从abc库中导入ABC, abstractmethod模块
from abc import ABC, abstractmethod


# 普通类
class P(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("say")

    @abstractmethod
    def hobby(self):  # 抽象方法
        pass


class S(P):

    def say(self):
        print('s say')

    def hobby(self):  # 实现抽象父类的抽象方法
        print("ball")


s = S(name="de", age=12)
s.say()
s.hobby()  # 子类实现抽象父类的抽象方法


# 抽象类
class A:
    def cool(self):
        pass

    def hot(self):
        pass

    def swing(self):
        pass


class Midea(A):
    def cool(self):
        print('M_cool')

    def hot(self):
        print('M_hot')

    def swing(self):
        print('M_swing')


class GREE(A):
    def cool(self):
        print('G_c')

    def hot(self):
        print('G_h')

    def swing(self):
        print('G_s')


def make(a: A):
    a.hot()
    a.cool()
    a.swing()


a: A  # 抽象类是不能实例化的 a被注解为A类型 a是A的子类的类型
a = Midea()
print('*' * 100)
a.swing()  # 输出M_swing
print('*' * 100)
x = Midea()
y = GREE()
make(x)
make(y)
