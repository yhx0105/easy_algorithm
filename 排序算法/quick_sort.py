# -*- coding: utf-8 -*-
def quick_sort(alist, first, last):
    '''快速排序'''
    if first>=last:
        return
    high = last - 1
    low = first
    mid_value = alist[first]
    while low < high:
        # high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # low右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 从循环退出，low=high
    alist[low] = mid_value

    # 对low左边的列表进行快速排序
    quick_sort(alist, 0, low - 1)

    # 对右边进行排序
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    alist = [3, 1, 4, 1, 5, 9, 2, 6]
    print(alist)
    li=quick_sort(alist, 0, len(alist))
    print(li)
