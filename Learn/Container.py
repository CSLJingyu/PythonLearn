# python中常用的容器
# list tuple str set dict

# list是可以修改的
my_list = [1, 2, 3]
my_list1 = [my_list, 4]
print('my_list:', my_list)  # [1, 2, 3]
print('my_list1:', my_list1)  # [[1, 2, 3], 4]

# list的索引
# 正向索引从0开始,最后一个元素为list的长度-1; 反向索引为最后一个为-1,倒数第二个元素的索引为-2, 第一个元素的索引为-列表长度
print('最后一个元素数值:', my_list[-3])  # 3

# 列表长度
print(f'列表长度: {len(my_list)}')

# 元组 一旦定义后,是不可以修改的, 不支持
# 元组名称 = (元素1, 元素2, ...)
# 一个元素的元组 = (元素1, )
# 空元组 = ()
my_tuple = ((1, 2, 3), ("a", "b", "c"))
print(my_tuple[0])  # (1, 2, 3)
# 元组.index(元素) 返回改元素的下表
# 元组.count(元素) 统计该元素出现的次数
# len(元组)  统计元组中的元素个数


# 字符串 str和以往用的一样


# 集合 set
# 集合名称 = {元素1, 元素2, .....}
# 集合的元素可以是多个数据类型,可以实现嵌套
# 是去重并且无序的
# 不支持索引访问
# 还有一些常见的操作 用的时候可以查询
my_set = {1, "de", ("q")}
for i in my_set:  # 依次输出元素
    print(i)
print(my_set)


# 字典
# 字典名称 = {key: value, key: value, ...}
# key不能重复,重复了会对前面的key的数值有影响
# 和set一样不支持下表索引
# 其他常见的用法 要用的时候搜索
my_dict = {'name':'jy', 'age':24}
print(f'my_dict:{my_dict}')  # jy
print('name:', my_dict['name'])
for key in my_dict:
    print(f'key:{key}, value:{my_dict[key]}')
print()
# items()返回一个视图对象,包含字典中key和value,这个视图对象的本质是可迭代的集合,一个元素是一个为(key, value)的元组
for key, value in my_dict.items():
    print(f'key{key}, value{value}')