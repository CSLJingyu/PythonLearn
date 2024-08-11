# 如果有很多文件 单独一个包进行管理
# 导入包 import 包名.模块名

def add(x, y):
    return x + y


if __name__ == '__main__':
    # 单独测试 别人调用的add函数不会执行这行代码
    print(f"测试add函数:  {add(1, 4)}")
