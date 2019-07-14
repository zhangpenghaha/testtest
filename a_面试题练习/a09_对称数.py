# 请用 python打印出10000以内的对称数(对称数特点:数字左右对称如:1,2,11,121,1221等

for i in range(10001):
    if i == int(str(i)[::-1]):
        print(i)