import json
import random

class Reg_data():

    def is_success(sef, num):
        # with open("E:/web_auto_wh/mytest/myproject/register/reg_data.json", encoding='utf-8') as f:
        #     test_data = json.load(f)


        users_list = {}
        for num in range(2):
            users = {
                'username': '15721064530',
                'verify_code': '8888',
                'pwd': '123456',
                'pwd2': '123456',
                'invite': '13333333333',
                'expect': '注册成功'
            }

            tel_num = "15" + str(random.randint(100000000, 999999999))
            users["username"] = tel_num
            users_list["is_succcess"+str(num)] = users
        print(users_list)

        with open("E:/web_auto_wh/mytest/myproject/register/reg_data.json", encoding="utf-8") as f:
            tel_errors = json.load(f)
            for key in users_list.keys():
                tel_errors[key] = users_list[key]
        print(tel_errors)
        tel_errors["name_error4"]["expect"] = "请用手机号或邮箱注册"
        with open("E:/web_auto_wh/mytest/myproject/register/reg_data.json","w",  encoding="utf-8") as f1:
            json.dump(tel_errors, f1)



if __name__ == "__main__":
    Reg_data().is_success(2)