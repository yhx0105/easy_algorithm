# -*- coding: utf-8 -*-
def selection_sort(alist):
    '''选择排序'''
    n = len(alist)
    for j in range(n-1):
        min=j
        for i in range(j+1,n):
            if alist[min]>alist[i]:
                min=i
        alist[j],alist[min]=alist[min],alist[j]

if __name__=='__main__':
    alist=[1,2,4,0,2,3,57,9,12]
    print(selection_sort(alist))
    print(alist)