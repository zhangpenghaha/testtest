# 需求 : 斐波那契数列求N
a =0
b =1
N = int(input("请输入N:"))
for i in range(1,N):
    a, b = b, a+b
print(a)
