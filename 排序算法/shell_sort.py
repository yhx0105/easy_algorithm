# -*- coding: utf-8 -*-
def shell_sort(alist):
    '''希尔排序'''
    n = len(alist)
    gap = 3
    while gap > 0:
        '''与插入算法的区别在于存在gap,gap变化到零之前变化的次数'''
        for j in range(gap, n):
            i = j
            while i >= gap:
                if alist[i] > alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i = i - gap
                else:
                    break
        gap = gap // 2
    return alist


if __name__ == '__main__':
    alist = [3, 1, 4, 1, 5, 9, 2, 6]
    print(alist)
    print(shell_sort(alist))
