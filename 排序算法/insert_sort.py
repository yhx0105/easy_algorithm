# -*- coding: utf-8 -*-
def inser_sort(alist):
    '''插入排序'''
    n=len(alist)
    for j in range(1,n):
        # 外层寻环
        i=j
        while i>0:
            if alist[i]<alist[i-1]:
            #从右边无序序列中取出第一个元素
                alist[i-1],alist[i]=alist[i],alist[i-1]
                i-=1
            else:
                break
    return alist
if __name__=='__main__':
    alist=[3,1,4,1,5,9,2,6]
    print(alist)
    print(inser_sort(alist))
