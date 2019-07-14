# 判断101-200之间有多少个素数,并输出所有的素数
num_count = 0
for i in range(101, 201):
    num =0
    for j in range(2, i+1):
        if i % j == 0:
            num += 1
    if num == 1:
        num_count += 1
        print(j)
print(num_count)
