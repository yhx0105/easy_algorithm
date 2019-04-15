# -*- coding: utf-8 -*-
# def bin_search(alist, target):
#     '''二分查找,递归版本'''
#     n = len(alist)
#     mid = n // 2
#     if n > 0:
#         if target < alist[mid]:
#             bin_search(alist[:mid], target)
#         elif target > alist[mid]:
#             bin_search(alist[mid + 1:], target)
#         else:
#             return mid


def bin_search_2(alist, target):
    '''非递归版本'''
    n=len(alist)
    first=0
    last=n-1
    while first<last:
        mid = (first + last) // 2
        if target>alist[mid]:
            first=mid+1
        elif target<alist[mid]:
            last=mid
        else:
            return mid


if __name__ == '__main__':
    target = 4
    alist = [1, 2, 4,7, 9]
    print(bin_search_2(alist, target))
