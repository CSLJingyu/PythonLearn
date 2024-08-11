# 类和对象
# 基于类创建对象
# 对象名 = 类名称()
# 调用成员方法/成员属性
# 对象名.成员方法/ 对象名.成员属性


class Person:

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 魔术方法 == 内置方法
    # 常见的有__str__， __lt__等等, __XX__这样的名字的就是魔术方法
    def __str__(self):
        print(f"name={self.name}, age={self.age}")

    def info(self):
        print(f"我的名字{self.name}, 年龄为{self.age}")

    def say(self, word):
        print(f"我说的{word}")


# 类的封装
class Private:
    name = None
    age = None
    # 两个下划线的变量表示私有变量 无法被对象所调用
    __money = 123

    def call(self, name):
        print(f'{self.name}')

    def __myMoney(self):
        print("私有成员方法")

    def use_private(self):
        # self.__money(self)
        if self.__money == 123:
            print("Yes")
        else:
            print("No")


# p = Private()
# p.name = "cd"
# p.age = 213
# p.call("cd")
# p.use_private()
# print(p.__money)  # AttributeError: 'Private' object has no attribute '__money'
# p.__myMoney()     # 'Private' object has no attribute '__myMoney'


# 类的继承
class Father:
    Frist_name = None
    age = None
    language = "fangyan"
    __money = 1000

    def __init__(self, Frist_name, age):
        self.Frist_name = Frist_name
        self.age = age

    def drink(self):
        print('drink')

    def say(self):
        print("你好")


class Mother:
    language = "Chinese"

    def say(self):
        print("Hello")


class Son(Father, Mother):  # 继承的原则是从左到右的优先级顺序,就是后面继承的会被前面继承的所覆盖

    ming = None

    def run(self):
        print('runing')


father = Father('L', 50)
son = Son("L", 26)
son.ming = "cd"
print(f'Frist name: {son.Frist_name}, ming: {son.ming}')
son.drink()
son.say()  # 你好
print(f"语言是:{son.language}")  # fangyan


# 复写
# 继承的成员属性和成员方法是可以进行改写的
# 一旦改写了,调用的就是改写后的内容
class small_son(Father, Mother):

    def run(self):
        print("playing")

    # 如果需要父类变量/方法的信息时
    # 1.使用父类名调用
    #   父类名.成员变量/成员方法

    # 2.使用super()调用
    #  super().成员变量
    #  super().成员方法()
    def say(self):
        super().age
        Father.say(self)  # 你好
        Mother.say(self)  # Hello


small = small_son("k", 12)
small.run()
small.say()


# 多态 常常用在继承上
# 同样的行为,传入不同的对象,得到不同的状态
class Animal:
    def speak(self):
        # 什么都不做,需要子类来复写
        pass


class Dog(Animal):
    def speak(self):
        print("dog")


class Cat(Animal):
    def speak(self):
        print("cat")


# 接受动物类型的对象
def lound(animal: Animal):
    animal.speak()


dog = Dog()
dog.speak()
cat = Cat()
cat.speak()
lound(dog)  # 输出dog
lound(cat)  # 输出cat
animal1: Animal  # animal1是Animal的一个实例或者是子类的一个实例
animal1 = Dog()
animal1.speak()  # 输出dog
