# -*- coding: utf-8 -*-
def merge_sort(alist):
    '''归并排序'''
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    # left_li 采用并归排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right_li采用并归排序后产生的新列表
    right_li = merge_sort(alist[mid:])
    #将两个列表合并成一个新的列表
    #merge（right_li,left_li）

    left_pointer,right_pointer=0,0
    result=[]

    while left_pointer<len(left_li) and right_pointer<len(right_li):
        if left_li[left_pointer]<right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer+=1
        else:
            result.append(right_li[right_pointer])
            right_pointer+=1

    result+=left_li[left_pointer:]
    result+=right_li[right_pointer:]
    return result

if __name__=='__main__':
    alist = [3, 1, 4, 1, 5, 9, 2, 6]
    print(alist)
    li=merge_sort(alist)
    print(li)