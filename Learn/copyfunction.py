# 浅拷贝深拷贝
# 开辟新的内存空间接受变量
# 调用id()可以获得变量的内存地址

# 浅拷贝
# 可变类型浅拷贝 list set bytearray
import copy

# 普通赋值
# 指向同一个空间
a = [1, 2]
b = a
print(id(a))
print(f"a: {a[0], a[1]}")
print(id(b))
print(f"b: {b[0], b[1]}")
print()

# 浅拷贝
# copy函数会开辟新的空间进行存储
# 不会拷贝对象内部的子对象
# 指向不同的空间
c = [[3], [4]]
d = copy.copy(c)
print(d)
print(id(c))
print(id(d))

# 不可变类型浅拷贝
# 不会给拷贝的对象进行开辟新的空间
e = (1, 2)
f = copy.copy(e)
print(f)
print(id(e))
print(id(f))

# 深拷贝
# 保证数据的独立性
# 对所有的数据并开辟对应的空间存储
# copy.deepcopy(拷贝对象)
print()
g = [1, 2]
h = copy.deepcopy(g)
print(id(g))
print(id(h))
print()

# eval函数
# 将字符串变为有效的表达式来进行求结果并且返回计算结果
# 开发的时候别用eval直接转input的结果 因为可能导致有些命令主机崩溃
res = eval("1 * 9 + 2")
print(res)
print()

# 将字符串转换为列表字典等
print(eval("[1, 2, 3]"))