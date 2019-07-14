# .阅读下面的代码，写出 A0，A1 至 An 的最终值？
# 1. A0 = dict(zip(('a'，'b'，'c'，'d'，'e')，(1，2，3，4，5)))
# 2. A1 = range(10)
# 3. A2 = [i for i in A1 if i in A0]
# 4. A3 = [A0[s] for s in A0]
# 5. A4 = [i for i in A1 if i in A3]
# 6. A5 = {i:i*i for i in A1}
# 7. A6 = [[i，i*i] for i in A1]
a = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(a)
b = range(10)
print(b)