# 了解使用timeit检测程序运行时间
from timeit import Timer


def t1():
    li = [i for i in range(10000)]


def t2():
    li = list(range(10000))


def t3():
    li = []
    for i in range(10000):
        li.append(i)


# def t4():
#     li = []
#     for i in range(10000):
#         li.insert(0, i)


timer1 = Timer('t1()', 'from __main__ import t1')
print(timer1.timeit(1000))

timer2 = Timer('t2()', 'from __main__ import t2')
print(timer2.timeit(1000))

timer3 = Timer('t3()', 'from __main__ import t3')
print(timer3.timeit(1000))

# timer4 = Timer('t4()', 'from __main__ import t4')
# print(timer4.timeit(1000))

li = list(range(11))
li[3:5] = range(1, 3)
print(li)
