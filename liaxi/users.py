import random

def user(user_num):
    """随机生成suer_num份"""
    # 清空文件
    with open("./card.txt", "w") as f:
        f.write('')

    for i in range(user_num):
        #  随机生成用户名
        tel_num = "13" + str(random.randint(1000000, 300000000))
        # 用户名账号密码保存到文件card.txt中
        list_tel = tel_num + ",123456" + ",8888" + "\n"
        with open("./card.txt", 'a') as f:
            f.write(list_tel)
    user_list = []
    with open("./card.txt",'r') as f2:
        user_1 = f2.readlines()
        # print(user_1)
        for line in user_1:
            user_list.append(line.split(","))
    return user_list

if __name__ == "__main__":
    user(5)