def desc():
    words = input("输入词句:")
    lists = words.split(" ")
    lists.reverse()
    for i in lists:
        print(i,end=' ')

desc()