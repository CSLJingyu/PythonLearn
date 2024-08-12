# 变量给出类型名称
var_1: int = 23


# 函数传参给出参数类型和返回类型
def add(x: int, y: int) -> int:
    return x + y


# 联合类型注解
# 在变量注解 函数形参和返回值注解中都可以用到
# 当数据类型不唯一的时候 用Union类型
from typing import Union
my_list: list[Union[str, int]] = [2, "de"]
my_dict: dict[str, Union[str, int]] = {"name": "dede", "age":34}


# 在函数中
def func(data: Union[int, str]) -> Union[int, str]:
    pass