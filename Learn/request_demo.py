# 爬虫
import requests
import re

url = 'https://www.weather.com.cn/weather1d/101010100.shtml'
# 打开浏览器并且打开网址
response = requests.get(url)

# 设置编码格式
response.encoding='utf-8'
# response响应对象, 对象.属性名 response.txt
print(response.text)

# 正则表达式 爬取指定的内容
city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', response.text)
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', response.text)
print(city)
print(weather)
print()

# 实现元素打包
lst = []
for a, b in zip(city, weather):
    lst.append([a, b])

for item in lst:
    print(item)

print('#' * 50)
# 将爬取结果保存在本地
with open(r'D:\Pycharm\PythonLearn\v.txt', 'w') as file:
    for item in lst:
        str = "--".join(item)
        file.write(str + '\n')


