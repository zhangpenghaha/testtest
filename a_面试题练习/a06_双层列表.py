# .python 两层列表怎么提取第二层的元素
aa = [[(55736,)], [(55739,)], [(55740,), (55801,)], [(55748,)], [(55783,), (55786,), (55787,), (55788,)], [(55817,), (55821,)], [(55818,)]]
for i in aa:
    for ii in i:
        print(ii)