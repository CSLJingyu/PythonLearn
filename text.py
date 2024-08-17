import os
import re


# 模型淘宝自动回复

def answer(question):
    with open('replay.txt', "r", encoding='utf-8') as file:
        math = re.search(r"订单", question)
        if math:
            answer_txt = file.readline()
            answer_txt = answer_txt.split('|')
            answer_txt = answer_txt[1].split()

        math = re.search(r"物流", question)
        if math:
            # 跳过第一行
            file.readline()
            answer_txt = file.readline().split()
            answer_txt = answer_txt.split('|')
            answer_txt = answer_txt[1].split()

        math = re.search(r"账户", question)
        if math:
            # 跳过第二行
            file.readline()
            file.readline()
            answer_txt = file.readline().split()
            answer_txt = answer_txt.split('|')
            answer_txt = answer_txt[1].split()

        math = re.search(r"支付", question)
        if math:
            # 跳过第三行
            file.readline()
            file.readline()
            file.readline()
            answer_txt = file.readline().split()
            answer_txt = answer_txt.split('|')
            answer_txt = answer_txt[1].split()

        return answer_txt


if __name__ == '__main__':
    get_answer = answer("订单")
    print(''.join(get_answer))
