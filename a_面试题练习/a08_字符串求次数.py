# 给定一个整数N,和一个0-9的数K,要求返回0-N中数字K出现的次数

N = int(input("请输入一个任意整数:"))
K = int(input("请输入一个0-9的数:"))
strs = ""
for num in range(N+1):
    strs += str(num)
a = strs.count(str(K))
print(a)