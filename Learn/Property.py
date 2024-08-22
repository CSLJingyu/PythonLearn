# Property 把类中的一个方法当作属性使用,实现简化开发
class Man:
    def __init__(self):
        # 私有属性
        self.__age = 23

    def age(self):
        return self.__age

    def set_age(self, new_age):  # 实现修改私有变量age的数值
        self.__age = new_age


man = Man()
print(f"man's age is {man.age()}")
man.set_age(120)
print(f"change man's age 23 to {man.age()}")


# 通过装饰器的方式使用
# @property表示把方法当作属性,表示当获取属性的时候,会执行下面的修饰方法 property修饰的方法名和属性名一样
# @方法名.setter表示把方法当作属性使用,表示当设置属性数值时候会执行下面修饰的方法
class P:
    def __init__(self):
        self.__age = 23

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age


p = P()
print(f'直接通过对象得到年龄属性:{p.age}')
print(f'直接通过方法修改属性')
p.age = 234
print(f'修改后年龄属性:{p.age}')


# 类属性方式使用
# property的参数说明
# 属性名 = property(获取值方法, 设置值方法)
# 第一个参数: 获取属性时需要用到的方法
# 第二个参数: 设置属性时需要用到的方法

class Woman:
    def __init__(self, name):
        self.__age = 29
        self.name = name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    @property
    def name(self):
        return self._name  # 单下滑线表示内部使用

    @name.setter
    def name(self, new_name):
        self._name = new_name

    # 类属性方式的property属性
    age = property(get_age, set_age)


woman = Woman("kk")
print(f'修改前的年龄: {woman.age}')
woman.set_age(345)
print(f"修改后的年龄: {woman.age}")

print(f"名字{woman.name}")
woman.name = "www"
print(f"名字{woman.name}")


# 上下文管理器
# 由实现__enter__()和__exit()__方法的类创建的对象
# __enter__表示上文方法, 需要返回一个操作文件对象
# __exit__表示下文方法, with语句执行完成会自动执行, 及时异常出现也会执行改方法
class File:
    def __init__(self, file_name, file_model):
        self.file_name = file_name
        self.file_model = file_model

    # 实现__enter__()方法
    def __enter__(self):
        print('这是上文')
        self.file = open(self.file_name, self.file_model)
        return self.file

    # 实现__exit__()方法
    # 实现资源在使用后的正确清理和释放
    def __exit__(self, exc_type, exc_value, traceback):
        print('这是下文')
        self.file.close()


# 使用with语句完成文件操作
with File(r"C:\Users\舒言\Desktop\X.txt", "w") as f:
    while True:
        user_input = input()
        if user_input.lower() == 'exit':
            break

        f.write(user_input + '\n')
