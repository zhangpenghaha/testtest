a = input("请输入单词: ")
dicts ={}
for i in a:
    num = a.count(i)
    if num >= 1:
        dicts[i] = num
print(dicts)