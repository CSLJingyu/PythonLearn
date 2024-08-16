class S:
    def __init__(self, id, age):
        self.id = id
        self.age = age

    def info(self):
        print(f"{self.id}, {self.age}")
        # return 12345


stu_list = []
for i in range(2):
    user_input = input()
    user_input = user_input.split("##")
    s = S(user_input[0], user_input[1])
    stu_list.append(s)

for i in range(len(stu_list)):
    print(stu_list[i].info())