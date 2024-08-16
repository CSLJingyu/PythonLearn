# python正则表达式
# 导入正则表达式的包
# 可以实现复杂的字符串匹配,搜索,替换问题
import re


# 不常见的自己要用的时候自己搜索
# 常见的如下

# 两个元素是否匹配一致
result = re.match(r'xdede', 'xdede')
if result:
    print('ok')
else:
    print('No')


# 全局搜索,返回第一个匹配的对象
# pattern是输入的目标对象, string是待匹配的对象
result = re.search(r'lk', 'lklslk')
if result:
    print('ok')
else:
    print('No')