import sys
# 中间的参数为mode 常见为w r a(追加)
with open(r"C:\Users\舒言\Desktop\text.txt", 'a') as f:
    f.write("dede")


# 在python的控制台中进行输入
with open(r"C:\Users\舒言\Desktop\X.txt", 'w') as file:
    # 在控制台实现输入
    while True:
        # 从控制台得到用户的输入
        user_input = input()

        # 检查是否退出输入
        if user_input.lower() == 'exit':
            break

        file.write(user_input + '\n')
    # i = 0
    # while i < 5:
    #     user_input = input()
    #     file.write(user_input + '\n')
    #     i = i + 1





